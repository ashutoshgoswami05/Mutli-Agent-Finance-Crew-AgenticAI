📈 Autonomous Financial Analyst Agent
A multi-agent system designed to act as an automated "Chief Investment Officer." It performs fundamental financial analysis, researches current market sentiment, and generates a final Buy/Sell/Hold recommendation.

🏗️ Architecture
The agent operates as a StateGraph, using a supervisor-analyst pattern to coordinate tasks.

Code snippet
graph LR
    A[Supervisor] --> B(Fundamental Analyst)
    B --> A
    A --> C(Sentiment Analyst)
    C --> A
    A --> D{Synthesis}
    D --> E[End]
Key Components:
Supervisor (Router): Manages the workflow, deciding whether to trigger the fundamental analyst, the sentiment analyst, or move to the final report synthesis.

Fundamental Analyst: Uses yfinance to retrieve real-time financial ratios (P/E, Debt-to-Equity, Revenue Growth).

Sentiment Analyst: Uses DuckDuckGoSearchRun to gather the latest market news and public sentiment regarding the ticker.

Chief Investment Officer (Synthesis): Combines the findings from both analysts to produce a definitive investment recommendation.

🛠️ Tech Stack
LangGraph: For managing the stateful agent workflow.

LangChain: For orchestrating LLM interactions and tool usage.

OpenAI GPT-4o: The core reasoning engine.

yfinance: To fetch real-time stock market data.

DuckDuckGo Search: For live market sentiment and news.
