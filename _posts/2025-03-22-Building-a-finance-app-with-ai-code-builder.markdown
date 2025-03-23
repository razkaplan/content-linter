---
layout: post
title: "I Vibe-Coded a Finance App: Turning Transactions into Investments"
publishedAt: "2025-03-20"
summary: "A weekend experiment to track my spending and turn it into an investment strategy—because if I believe in a product, why not own part of the company?"
" 
---

## **A GTM Experiment Disguised as a Finance App**

As a creative marketer, I spend a lot of time thinking about **how products evolve from an idea to something people actually use**. Sometimes, that means building quick experiments myself—especially when a concept sticks in my mind.

Last weekend, I built a simple finance tool. **The idea?** If I keep buying certain products, should I also be investing in the companies behind them? Can I **automate** that insight and scale it?

### **The Inspiration: Shopping as an Investment Signal**

It started with a podcast. A hedge fund manager mentioned one of his investment strategies: **analyzing his own shopping behavior** to identify publicly traded companies worth investing in.

That got me thinking—**can I automate this?** Can I scan my credit card expense reports from the past year and literally put my money where my mouth is?

TL;DR – Yes. But it’s not as easy as it sounds.

## **Step 1: Manual Testing – Does This Even Work?**

Before writing a single line of code, I **tested the concept manually**. Looking at one month of transactions, I found that:

* I had purchased from **five publicly traded companies**.  
* The **average stock return** since my purchase date was **70%**.

That was enough to validate that **the idea had merit**. Time to automate.

---

## **Step 2: Automating the Analysis with AI & APIs**

To scale this, I started experimenting with **vibe-coding tools** (Cursor, Claude, Windsurf, and OpenAI APIs).

### **The Hardest Part: Parsing Bilingual PDFs**

Credit card statements aren’t developer-friendly—especially when they switch between **Hebrew and English**. It took **50+ API calls** across different AI models to get a structured dataset. And even then, the system was far from perfect.

### **Extracting Publicly Traded Companies**

I downloaded **global stock market data** to match transactions to companies. Since I live in Israel and travel a lot, I needed a solution that worked across markets.

Then, Windsurf suggested a shortcut: **the Yahoo Finance API**. It simplified things but still didn’t recognize every company.

Now, the tool generates a table like this:

| Company | Symbol | Date of Transaction | Cost | Stock Change (%) | Stock Change (USD) |
| :---: | :---: | :---: | :---: | :---: | :---: |

### **Next Iteration: Expanding to Grocery & B2B Brands**

Some of the companies I buy from aren’t consumer brands (e.g., **P\&G, Unilever**). The next step is to **map purchases to parent companies** and **expand to non-B2C stocks**.

---

## **Step 3: The Results – What If I Had Invested in My Own Spending?**

If, in 2024, I had **doubled my spending** by investing the same amount in stocks, my **return would have been 40%**.

For comparison, the **S\&P 500 returned 23%** in the same timeframe.

---

## **Try It Yourself (No Data Stored\!)**

[Try it out](https://expense2invest.streamlit.app/) – it runs in your browser, and I don’t store any data.

This is just an experiment, but if you find it useful, **feel free to fork the repo and improve it**.

📌 [Check out the GitHub project](https://github.com/razkaplan/smart-expense-tracker) – contributions welcome\! Let’s build something smarter together.

---

## **Why This Matters for Early-Stage GTM Strategy**

This wasn’t just a finance experiment—it was a **GTM thought exercise**:

* **Rapid validation:** Tested manually before automating.  
* **Tech stack experimentation:** Used AI tools to speed up development.  
* **Market insights:** Real-world behavior as an investment signal.

This approach applies to **any early-stage product**—whether it’s fintech, SaaS, or AI-driven growth. If you’re a founder looking to validate and scale an idea, **let’s talk**. 🚀
