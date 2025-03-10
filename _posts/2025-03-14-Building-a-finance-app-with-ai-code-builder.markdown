---
layout: post
title: "My app is cool"
publishedAt: "2025-03-14"
summary: "Introducing: Transactions to investments - put your money where your mouth is" 
---

I took the weekend to work on a simple finance tool.
This tool can inspire Product managers and founders in the finance industry to build a more robust solution that meet these needs. 

I listend to a podcast interview with a hedgefund manager, he says that one of his stratgies is looking at his own shopping behaivor, and see if the products he purchase are coming from publicly traded companies. 
So, it got me thinking - Can I scale it? 
Can I scan my credit card expansion reports from the last year and literally put my money where my mouth is? 
TL;DR - Yes. 
The hardest part was reading a bi-lingual PDF. 
Next step was extracting transactions that are publicly traded. I've downloaded the list of all publicly traded companies from all over the world. Since I live in Israel and travel a lot, I figured, why not? 

So now I have this CSV with companmy, global symbol, date of tranasaction and cost in USD. I've reached out to yahoo finance API to find the cost of stock on the transaction date. 

Now the table look like this - Company, Symbol, date of transaction, cost, change of stock from this date to today in %, and in USD, based on the cost. 

Next, I did the same thing for my groccery shopping cart, to get access to non b2c brands like P&G. 

To summarize, in 2024, if I would have doubled my investment and for each product, purchase a stock, for the same price, my money will return X3. 

For refrence, S&P did XX in the same time. 

Try it out yourself. I don't keep any information on the server, I've added links to interactive brockers. 

Download the free gmail extension - it does the exact same thing automatically 