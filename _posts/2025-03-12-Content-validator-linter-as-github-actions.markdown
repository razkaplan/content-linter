---
layout: post
title: "Thoughts of using GitHub to manage content, with co-pilot and GitHub Actions"
publishedAt: "2025-03-12"
summary: "Exploring the use of GitHub and visual studio for content management, leveraging GitHub Copilot and GitHub Actions. This post introduces a custom-built Content Linter GitHub Action designed to ensure blog posts meet technical SEO requirements and include relevant keywords."
---

When I worked at a dev-tool company, they required everything we posted to go through GitHub, including blogs. As a marketer, I wasn't used to working that way, but as a former journalist and content writer, I found the idea of an approval mechanism that requires reviews, both automated and manual, fascinating.

Getting closer to developers exposed me to the simple yet clever idea of GitHub Actions and automated checks and tests. So I figured, why not have a simple tool that will act similar to YoastSEO, but inside GitHub, only for blog posts?

What's even cooler is that I used GitHub Copilot in VS Code to build the linter, only "code vibing". Additionally, since Copilot is powered by GPT-4, I'm using it to edit and proofread this blog! This makes my process fast and accurate. For now, VS Code is my WordPress.

I invite you to install the Action, and if you are a developer, I invite you to contribute to the project.

In the next steps, I'm looking to add spell check and brand-voice checker.

## Introducing the Content Linter GitHub Action

The Content Linter GitHub Action is designed to help you ensure that your blog posts meet technical SEO requirements and include relevant keywords. It performs two main checks:

1. **Technical SEO**: Ensures that all titles, descriptions, and images exist and are described as needed. It also checks for broken links.
2. **Keywords**: Ensures that one or more of the declared keywords appear in relevant places. The declared keywords are stored in a configuration file called `keywords.txt`.

### How to Use the Content Linter

To get started with the Content Linter, follow these steps:

Simply add it from Github actions marketplace
