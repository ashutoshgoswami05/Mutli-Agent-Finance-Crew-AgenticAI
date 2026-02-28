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
5. **SEC & Earnings Analyst** retrieves most recent earnings call transcript via RAG
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

Below is an example of the kind of clear, structured investment recommendation the Autonomous Financial Analyst Agent produces after synthesizing financial metrics, market sentiment, and qualitative insights from SEC filings and recent developments.


# Investment Recommendation

**Ticker:** AAPL  
**Recommendation:** ⚖️ **Hold**  
**Confidence:** Moderate  
**Date:** February 28, 2026

Apple Inc. continues to exhibit strong underlying business performance, but faces a combination of elevated leverage, regulatory headwinds, and near-term strategic uncertainty.

## Key Financial Metrics

- **P/E Ratio:** 33.44  
  → Investors are willing to pay a premium for AAPL’s earnings, reflecting strong confidence in future growth — particularly in services and AI — but also raising questions about valuation stretch.

- **Debt-to-Equity Ratio:** 102.63%  
  → Significant leverage increases financial risk, especially in a higher interest rate environment or if consumer spending softens.

- **Revenue Growth:** 15.7%  
  → Solid expansion continues to support the high valuation, driven by services strength and an enormous active installed base.

## Market Sentiment & Recent Developments

- **Regulatory Pressure**  
  Ongoing Department of Justice antitrust lawsuit targeting potential opening of iMessage and Apple Pay ecosystems — a material long-term risk to ecosystem control and margins.

- **Stock Price Action**  
  Recent >10% decline primarily attributed to management changes and investor concerns around AI strategy execution rather than deterioration in core fundamentals.

- **Earnings Outlook**  
  Upcoming quarterly report carries cautious optimism — investors are particularly focused on AI positioning progress and sustained services revenue momentum.

## Insights from Recent SEC Filings & Statements

- High customer satisfaction scores and continued robust growth in the Services segment  
- Substantial active device installed base providing long-term revenue stability  
- Notable tariff-related cost pressures currently weighing on profitability  
- Overall narrative of operational resilience and product momentum despite external challenges

## Final Assessment

Apple maintains **very strong fundamentals** — impressive revenue growth, profitability, ecosystem lock-in, and services momentum — but is currently offset by:

- Elevated balance sheet leverage  
- Active antitrust/regulatory scrutiny  
- Near-term uncertainty around AI execution and leadership transitions

**Recommended Action:**  
**Hold** existing positions.  
Monitor closely for:  
• Clarity on antitrust outcomes and potential ecosystem changes  
• Evidence of successful AI monetization in upcoming earnings  
• Any signs of deleveraging or margin improvement  
• Broader market reaction to management strategy updates

The recent price pullback appears more sentiment-driven than fundamental — creating a possible stabilization or re-rating window if risks are contained.

---
*This analysis is for informational and educational purposes only. It is not investment advice.*
<br>
