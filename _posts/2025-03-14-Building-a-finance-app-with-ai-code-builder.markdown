---
layout: post
title: "I vibe coded a finance app"
publishedAt: "2025-03-20"
summary: "Introducing: Transactions to investments - put your money where your mouth is" 
---

## The Idea: Can Your Shopping Habits Guide Investments?  

I spent the weekend working on a simple finance tool. **TL;DR – It wasn’t that easy.**  

This tool can inspire **product managers and founders in the finance industry** to build more **intuitive** and **automated** solutions for tracking consumer-driven investments.  

![My Example](_data/images/expenses-public-traded.png)  

I was listening to a podcast interview with a **hedge fund manager** who shared an interesting investment strategy:  

> "I analyze my **own shopping behavior** to see if the products I buy come from **publicly traded companies**. If they do, I consider investing in them."  

That got me thinking:  
- **Can I scale this?**  
- **Can I scan my credit card expense reports from the past year and literally put my money where my mouth is?**  

**TL;DR – Yes. But it’s quite difficult.**  

---

## The First Attempt: Manual Tracking  

I first tried doing this manually and found that, in a specific month, I had shopped from **five public companies**. If I had invested in their stocks at the time of purchase, I would have seen an **average return of 70%** from then to today.  

That looked promising, so I decided to **automate and scale it**.  

---

## Automating the Process with AI and APIs  

I started experimenting with **vibe-coding tools** to extract transaction data and match it to publicly traded companies.  

### 🔹 Challenge #1: Parsing Bilingual PDFs  
The hardest part was reading **bilingual PDF** statements. It took **50+ credits** across **Windsurf, Cursor, and Claude** just to get a functioning system—and it’s still far from perfect.  

### 🔹 Challenge #2: Identifying Publicly Traded Companies  
At first, I downloaded a **global list** of publicly traded companies. Since I live in Israel and travel frequently, I wanted to cover **multiple stock markets**.  

Then, **Windsurf suggested a better approach**: using the **Yahoo Finance API** instead. But even that doesn’t recognize all companies, so there's still work to be done.  

---

## The Final Output: A Simple Investment Dashboard  

Now, my table looks like this:  

| **Company** | **Symbol** | **Date of Transaction** | **Cost** | **Stock Change (%)** | **Stock Change ($)** |  
|------------|----------|---------------------|------|------------------|------------------|  
| Example Corp | XYZ | 2024-01-15 | $50 | +12% | +$6 |  
| Another Co | ABC | 2024-02-10 | $80 | -5% | -$4 |  

### Next Steps: Expanding to Grocery Purchases  
In the next version, I plan to apply the same logic to my **grocery shopping cart**, mapping purchases to **non-B2C brands** like **Procter & Gamble (P&G)** to uncover hidden investment opportunities.  

---

## The Results: What If I Had Invested?  

If, in 2024, I had **doubled my investment**—buying **stocks equal to my spending** for each product—I would have seen a **return of 40%**.  

For reference, the **S&P 500** had a **23%** return over the same period.  

[🚀 Try it out](https://expense2invest.streamlit.app/)  

---

## Contribute & Improve the Project  

This is just for **inspiration**—I don’t store any data on a server, and you can run it **locally** for full control.  

Want to **improve it**? You're welcome to contribute!  

👉 **Check out the GitHub repo:** [smart-expense-tracker](https://github.com/razkaplan/smart-expense-tracker)  

Ways you can help:  
- Improve **PDF parsing** and **multi-language support**  
- Enhance **company-matching accuracy** (Yahoo API misses some)  
- Expand support for **non-B2C brands**  

Let’s build something cool together! 🚀