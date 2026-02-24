📈 Autonomous Financial Analyst Agent

An intelligent multi-agent system designed to function as an automated Chief Investment Officer (CIO).
It performs fundamental financial analysis, evaluates real-time market sentiment, and delivers a clear Buy / Sell / Hold recommendation — all autonomously.

🏗️ Architecture

The system is built using a StateGraph with a Supervisor–Analyst pattern, ensuring structured, stateful decision-making across multiple agents.

🔑 Key Components
🧭 Supervisor (Router)

Orchestrates the workflow

Decides whether to:

Trigger the Fundamental Analyst

Trigger the Sentiment Analyst

Proceed to Final Synthesis

Maintains state across the graph

📊 Fundamental Analyst

Retrieves real-time financial metrics using yfinance

Analyzes:

Price-to-Earnings (P/E) Ratio

Debt-to-Equity Ratio

Revenue Growth

Produces a structured financial health assessment

📰 Sentiment Analyst

Uses DuckDuckGoSearchRun to gather:

Latest market news

Public sentiment

Emerging narratives around the ticker

Evaluates overall bullish or bearish tone

🧠 Chief Investment Officer (Synthesis)

Combines:

Quantitative financial data

Qualitative market sentiment

Produces a definitive:

✅ Buy
⚖️ Hold
❌ Sell

Includes clear reasoning and risk considerations

🛠️ Tech Stack
Component	Purpose
LangGraph	Stateful multi-agent workflow orchestration
LangChain	Tool integration and LLM coordination
OpenAI GPT-4o	Core reasoning engine
yfinance	Real-time financial data retrieval
DuckDuckGo Search	Live news & sentiment analysis
🚀 How It Works (Flow Summary)

User inputs a stock ticker

Supervisor routes tasks to analysts

Analysts return structured findings

CIO agent synthesizes insights

Final investment recommendation is generated

🎯 Design Philosophy

Modular & extensible

Transparent reasoning

Real-time data driven

Clear, actionable output
