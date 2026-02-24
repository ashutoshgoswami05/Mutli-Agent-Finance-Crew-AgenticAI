# Autonomous Financial Analyst Agent 📈

An intelligent **multi-agent system** that acts as an automated **Chief Investment Officer (CIO)**.

Performs **fundamental analysis**, evaluates **real-time market sentiment**, and delivers clear **Buy / Sell / Hold** recommendations — fully autonomously.

<br>

## ✨ Key Features

- Real-time financial data via **yfinance**
- Live news & sentiment analysis using web search
- Multi-agent architecture with supervisor routing
- Transparent, structured reasoning
- Clear, actionable investment recommendation
- Modular and easy to extend

<br>

<br>

## 🔑 Agents & Responsibilities

| Agent                | Purpose                                                                 | Main Data Sources          | Output                              |
|----------------------|-------------------------------------------------------------------------|----------------------------|-------------------------------------|
| **Supervisor**       | Orchestrates workflow, decides next step, maintains state              | —                          | Routing decision                    |
| **Fundamental Analyst** | Analyzes core financial health (P/E, D/E, growth, margins, etc.)     | yfinance                   | Structured financial assessment     |
| **Sentiment Analyst**   | Gathers latest news, social sentiment, emerging narratives             | DuckDuckGo Search / web    | Bullish / Bearish / Neutral score   |
| **CIO (Synthesis)**     | Combines quant + qual insights, weighs risks, makes final call         | Outputs from both analysts | Buy / Hold / Sell + detailed reasoning |

<br>

## 🛠️ Tech Stack

| Component       | Purpose                                  |
|-----------------|------------------------------------------|
| **LangGraph**   | Stateful multi-agent workflow            |
| **LangChain**   | Tool integration & LLM chaining          |
| **OpenAI GPT-4o** | Core reasoning & synthesis             |
| **yfinance**    | Real-time stock metrics & fundamentals   |
| **DuckDuckGo Search** | Live news & market sentiment         |

<br>

## 🚀 How It Works – Flow Summary

1. User provides a stock ticker (e.g. `AAPL`, `TSLA`, `NVDA`)
2. Supervisor routes work to Fundamental Analyst
3. Fundamental Analyst pulls & interprets key ratios
4. Supervisor triggers Sentiment Analyst
5. Sentiment Analyst scans recent news & public narrative
6. CIO Agent receives both reports → synthesizes → decides
7. Final output: **Recommendation + Confidence + Key Reasons + Risks**

<br>

## 🎯 Design Goals

- **Modular** – easy to add new analysts (technical, macro, options, ESG…)
- **Transparent** – every agent shows reasoning
- **Real-time** – leverages fresh market data & news
- **Actionable** – clear Buy/Hold/Sell + risk context
- **Stateful** – remembers previous steps & decisions

<br>
