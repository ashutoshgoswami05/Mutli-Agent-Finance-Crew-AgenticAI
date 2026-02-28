# Autonomous Financial Analyst Agent 📈

An intelligent **multi-agent system** that acts as an automated **Chief Investment Officer (CIO)**.

Performs **fundamental analysis**, evaluates **real-time market sentiment**, and delivers clear **Buy / Sell / Hold** recommendations — fully autonomously.

<br>

## ✨ Key Features

- Real-time financial metrics & ratios via **yfinance**
- Live news & market sentiment via web & social search
- **RAG over earnings call transcripts** 
  → Provides deep qualitative context (management tone, forward guidance, risk factors, MD&A, strategic priorities) directly to the LLM
- Multi-agent architecture with supervisor routing
- Transparent, structured reasoning with source citations
- Clear, actionable investment recommendation with confidence & risk assessment
- Modular and easy to extend

<br>

## 🔑 Agents & Responsibilities

| Agent                     | Purpose                                                                                   | Main Data Sources                              | Output                                      |
|---------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------|---------------------------------------------|
| **Supervisor**            | Orchestrates workflow, decides next step, maintains state                                | —                                              | Routing decision                            |
| **Fundamental Analyst**   | Analyzes core financial health (P/E, D/E, growth, margins, profitability, etc.)         | yfinance                                       | Structured financial assessment             |
| **Sentiment Analyst**     | Gathers latest news, social sentiment, emerging narratives                               | Web search, X (Twitter), financial news        | Bullish / Bearish / Neutral score + summary |
| **Earnings Analyst**| Retrieves & reasons over **earnings call transcripts** via RAG |  
| **CIO (Synthesis)**       | Combines quantitative metrics + sentiment + qualitative SEC/earnings context, weighs risks, makes final call | Outputs from all analysts                      | Buy / Hold / Sell + detailed reasoning + confidence + sources |

<br>

## 🛠️ Tech Stack

| Component              | Purpose                                           |
|------------------------|---------------------------------------------------|
| **LangGraph**          | Stateful multi-agent workflow                     |
| **LangChain**          | Tool integration, LLM chaining, RAG pipelines     |
| **OpenAI GPT-4o**      | Core reasoning, synthesis & tool use              |
| **yfinance**           | Real-time stock metrics & fundamentals            |
| **DuckDuckGo Search**  | Live news & broad market sentiment                |
| **SEC → Vector** | Earning calls transciptions chunked and added to context |
| **Earnings calls**     | Seeking Alpha / BamSEC / AlphaSense API / web scrape (varies by implementation) |

<br>

## 🚀 How It Works – Flow Summary

1. User provides a stock ticker
2. Supervisor routes tasks
3. **Fundamental Analyst** pulls & interprets key ratios
4. **Sentiment Analyst** scans recent news & public narrative
5. **SEC & Earnings Analyst** retrieves relevant sections from latest 10-K/10-Q + most recent earnings call transcript via RAG
6. Agents return structured findings with sources
7. **CIO agent** synthesizes quantitative + sentiment + deep qualitative context
8. Final output: **Recommendation + Confidence + Key Reasons + Risks + Citations**

<br>

## 🎯 Design Goals

- **Modular** – easy to add new analysts (technical, macro, options, ESG, activist holdings…)
- **Transparent** – every agent shows reasoning + sources / filing dates / transcript quotes
- **Real-time & deep** – combines fresh market data, news **and** authoritative SEC / earnings call context
- **Factual grounding** – RAG over primary sources (filings & calls) significantly reduces hallucination on qualitative topics
- **Actionable** – clear Buy/Hold/Sell + risk context + what would change the thesis

<br>


## Sample Output

Below is an example of the kind of clean, structured investment recommendation the Autonomous Financial Analyst Agent produces after synthesizing fundamental data and market sentiment.


# Investment Recommendation

**Ticker:** AAPL  
**Recommendation:** ⚖️ **Hold**  
**Confidence:** Moderate  
**Date:** February 24, 2026

Apple Inc. presents a mixed investment profile with both opportunities and risks.

## Key Strengths
- **Strong Growth Potential**  
  High P/E ratio reflects market optimism about future earnings, backed by solid **15.7% revenue growth** — driven by consistent product innovation, services expansion, and ecosystem strength.

## Key Concerns
- **Elevated Leverage**  
  Debt-to-Equity ratio of **102.63%** signals meaningful balance sheet debt. While Apple’s exceptional cash flows and market leadership provide a buffer, this level of leverage introduces risk if macro conditions weaken or interest rates remain high.

- **Neutral Technical & Sentiment Picture**  
  RSI at **46.69** and current neutral market sentiment suggest the stock is neither overbought nor oversold. It is likely to trade sideways until a clear catalyst appears (new product cycle, major services milestone, updated guidance, etc.).

## Final Assessment
While Apple continues to demonstrate **very strong financial health**, **dominant competitive positioning**, and credible long-term growth drivers, the current combination of a **rich valuation** and **notable leverage** justifies caution.

**Recommended Action:**  
Maintain existing positions (**Hold**).  
Wait for either:  
• Positive catalysts that could justify the premium valuation  
• A more attractive entry point  
• A material improvement in the risk/reward profile

Investors with shorter horizons or lower risk tolerance may consider trimming on strength; very long-term holders can reasonably keep current weightings.

---
*This analysis is for informational and educational purposes only. It is not investment advice.*
<br>