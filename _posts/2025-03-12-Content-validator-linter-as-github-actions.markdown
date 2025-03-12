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

## Release Notes: Content Linter GitHub Action v1.0.0

### Overview

We are excited to announce the release of the Content Linter GitHub Action! This action is designed to help you ensure that your blog posts meet technical SEO requirements and include relevant keywords. It performs two main checks:

1. **Technical SEO**: Ensures that all titles, descriptions, and images exist and are described as needed. It also checks for broken links.
2. **Keywords**: Ensures that one or more of the declared keywords appear in relevant places. The declared keywords are stored in a configuration file called `keywords.txt`.

### Features

- **Technical SEO Validation**: Automatically checks for the presence of titles, descriptions, and images in your blog posts. It also verifies that there are no broken links.
- **Keyword Validation**: Ensures that your blog posts contain one or more of the declared keywords, helping you maintain relevance and improve SEO.
- **Spell Check**: Utilizes the `pyspellchecker` Python library to automatically detect and correct spelling errors in your blog posts, ensuring your content is free from typos and spelling mistakes.
- **Easy Integration**: Seamlessly integrates with your GitHub repository. Simply add the action to your workflow, and it will run on every push and pull request that affects your blog posts.

### How to Use

To get started with the Content Linter, simply add it from the [GitHub Marketplace](https://github.com/marketplace/actions/content-linter).

### Contribute

I welcome contributions from the community! If you have ideas for new features or improvements, please open an issue or submit a pull request.

---

I hope you find the Content Linter GitHub Action useful for maintaining high-quality blog posts. Happy blogging!
