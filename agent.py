# %%
from typing import TypedDict, Annotated, List, Dict, Optional
from langgraph.graph import END, StateGraph
import operator
# %%
import yfinance as yf

# %%
import os
from dotenv import load_dotenv


class FinancialData(TypedDict):
    ratios: Dict
    earnings_trend: str
class SentimentData(TypedDict):
    score: float
    summary: str
class InvestmentState(TypedDict):
    ticker: str
    question:str
    answer: str       
    messages: Annotated[List[str],operator.add]
    fundamental_data: Optional[FinancialData]
    Sentiment_data: Optional[SentimentData]
    Context_data: Annotated[List[str],operator.add]
   

    current_step: str
    is_debated: bool


# 1. Load the variables from .env into the environment
load_dotenv()

# 2. Retrieve the key
api_key = os.getenv("OPEN_API_KEY")

if not api_key:
    raise ValueError("API Key not found. Please set it in the .env file.")

print("Key loaded successfully!")

# %%
###{'pe_ratio': 33.4488, 'debt_to_equity': 102.63, 'revenue_growth': 0.157###

# %%
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage

# %%
from langchain_community.tools import YahooFinanceNewsTool
from langchain.tools import tool
import yfinance as yf

@tool

def get_fundamental_metrics(ticker: str):
    """Fetches P/E, Debt-to-Equity, and Revenue Growth for a given ticker."""
    stock = yf.Ticker(ticker)
    info = stock.info
    
    return {
        "pe_ratio": info.get("trailingPE"),
        "debt_to_equity": info.get("debtToEquity"),
        "revenue_growth": info.get("revenueGrowth"),
    }

tools = [get_fundamental_metrics]

from langchain_openai import ChatOpenAI

# Initialize the LLM with tool binding
llm = ChatOpenAI(model="gpt-4o",api_key=api_key).bind_tools(tools)
def fundamental_analyst_node(state :InvestmentState):
    ticker= state['ticker']

    prompt=f""" 
You are an expert Fundamental Analyst. Analyze the financial metrics for {ticker}

1. Use the 'get_fundamental_metrics' tool to retrieve current data.

2. Assess the financial health based on P/E and Debt/Equity.

3. Return a concise, structure analysis.


 """

    response= llm.invoke([("system", prompt),("human" , f"Analyze {ticker}")])

    if response.tool_calls:

        tool_name = response.tool_calls[0]["name"]
        tool_args = response.tool_calls[0]["args"]
    
    if tool_name == "get_fundamental_metrics":
        tool_result = get_fundamental_metrics.invoke(tool_args)

        print(f"tools result {tool_result}")

        messages = [
            SystemMessage(content=prompt),
            HumanMessage(content=f"Analyze {ticker}"),
            response, # Pass the AIMessage object directly
            ToolMessage(
                tool_call_id=response.tool_calls[0]["id"],
                content=str(tool_result)
            )
        ]
        
        final_response = llm.invoke(messages)

        state['fundamental_data']=final_response.content

    else:

        state['fundamental_data']=response.content

    return state

# %%
def router(state: InvestmentState):

    fund = state.get("fundamental_data")
    sent = state.get("Sentiment_data")
    context=state.get("Context_data")
    
    if fund and sent and context:
        return {"current_step": "synthesis"}
    elif not fund:
        return {"current_step": "fundamental_analyst"}
    elif not sent:
        return {"current_step": "sentiment_analyst"}
    elif not context:
            return {"current_step": "retrieve"}
    else:
        return {"current_step": "synthesis"}
        

# %%
def route_after_supervisor(state: InvestmentState):

    return state["current_step"]

# %%
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

def sentiment_analyst_node(state: InvestmentState):
    ticker = state["ticker"]
    
    results = search_tool.invoke(f"market sentiment and news for {ticker}")

    state['Sentiment_data']=results

    return state

# %%
from earningscall import get_company
from langchain_core.documents import Document 
from langchain_text_splitters import RecursiveCharacterTextSplitter

def retrieve_earningcall(ticker='aapl'):

    company = get_company(ticker)  


    transcript1 = company.get_transcript(year=2025, quarter=3, level=4)

    docs = [
        Document(
            page_content=transcript1.prepared_remarks,
            metadata={"section": "prepared_remarks"}
        ),
        Document(
            page_content=transcript1.text,
            metadata={"section": "discussion"}
        )
    ]

    return docs

def chunk_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200,
    chunk_overlap=200
)

    chunked_docs = splitter.split_documents(docs)


    return chunked_docs

# %%
def filter_docs(docs):

    docs_filterd=[]
    for chunk in docs:
        docs_filterd.append(chunk.page_content)

    return docs_filterd


# %%
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

def retrieve_chunks(chunks, query, top_k=5):
        model = SentenceTransformer("all-MiniLM-L6-v2")
        chunk_embeddings =model.encode(chunks, convert_to_numpy=True)
        query_embedding = model.encode([query], convert_to_numpy=True)

        similarities = cosine_similarity(query_embedding, chunk_embeddings)[0]
        
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        return [chunks[i] for i in top_indices]


def earnings_rag_runtime(filter_docs,query,top_k):
    top_chunks = retrieve_chunks(filter_docs, query, top_k)
    return top_chunks

def retrieve_node(state: InvestmentState):
    print("---RETRIEVING CONTEXT---")
    
    ticker=state.get('ticker')
    question=state.get('question')

    docs=retrieve_earningcall(ticker)
    docs=chunk_docs(docs)
    filtered=filter_docs(docs)
    
    best_chunks = earnings_rag_runtime(filtered, question,top_k=3)

    state["Context_data"]=[best_chunks]
    return state

# %%
def synthesis_node(state: InvestmentState):
    """
    Acts as the 'Chief Investment Officer'. 
    Reads the Fundamental and Sentiment data and produces a final verdict.
    """
    # 1. Access both data sources
    fund_data = state.get("fundamental_data", {})
    sent_data = state.get("Sentiment_data", {})
    question=state.get("question",{})
    context=state.get("Context_data",{})

   # print(f"context_data: {context}")


    #print(f" fundamental data {fund_data} sentimental_data={sent_data}")
    # 2. Instruct the LLM to synthesize
    prompt = f"""
    You are the Chief Investment Officer. Synthesize this data for {state['ticker']}:
    Fundamental: {fund_data}
    Sentiment: {sent_data}

    Also answer user's question: {question} considering the sec statements and filings {context}
    
    Produce a final Buy/Sell/Hold make it BOLD and underlined and in the next line give recommendation with a clear rationale also based on the context.

    
    """
    
    # 3. Generate report
    response = llm.invoke(prompt)

    #print(f"final analyst data : {response.content}")
    
    state['messages']=[response.content]

    return state

# %%


graph= StateGraph(InvestmentState)
graph.set_entry_point("supervisor")
graph.add_node("fundamental_analyst",fundamental_analyst_node)
graph.add_node("sentiment_analyst",sentiment_analyst_node)
graph.add_node("retrieve",retrieve_node)
graph.add_node("supervisor",router)
graph.add_node("synthesis",synthesis_node)


graph.add_conditional_edges(
    "supervisor",
    route_after_supervisor, # This reads the state update from the router node
    {
        "fundamental_analyst": "fundamental_analyst",
        "sentiment_analyst": "sentiment_analyst",
        "retrieve":"retrieve",
        "synthesis": "synthesis",
        "__end__": END
    })
graph.add_edge("fundamental_analyst", "supervisor")
graph.add_edge("sentiment_analyst", "supervisor")
graph.add_edge("retrieve", "supervisor")
graph.add_edge("synthesis", END)


graph_application= graph.compile()

# # %%
# from IPython.display import Image, display
# Image(app.get_graph().draw_mermaid_png())

# # %%
# # Invoke the graph
# final_state = app.invoke(
#     {"ticker": "AAPL", "current_step": "supervisor","question": "how is the stock performing should i buy it"}, 
#     config={"recursion_limit": 10}
# )
# # Print the results
# print("--- Final State ---")
# from IPython.display import display, Markdown



# # # %%
# display(Markdown(final_state.get("messages")[-1]))


