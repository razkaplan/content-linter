---
layout: post
title: "Thoughts of using GitHub to manage content, with co-pilot and GitHub Actions"
publishedAt: "2025-03-12"
summary: "Exploring the use of GitHub and visual studio for content management, leveraging GitHub Copilot and GitHub Actions. This post introduces a custom-built Content Linter GitHub Action designed to ensure blog posts meet technical SEO requirements and include relevant keywords."
---

## Managing Content Like Code: A Marketer’s Journey

When I worked at a dev-tool company, everything—blogs included—had to go through GitHub. As a marketer, this was unfamiliar territory, but my background in journalism and content writing made me appreciate the structured review process. Having automated and manual approvals felt like a game-changer for content quality.

As I spent more time with developers, I became fascinated by GitHub Actions and automated checks. That’s when I thought: Why not build a tool similar to YoastSEO, but integrated into GitHub, specifically for blog posts?

## Introducing the Content Linter GitHub Action

To make this idea a reality, I used GitHub Copilot in VS Code to build the Content Linter—essentially just "code vibing." Copilot, powered by GPT-4, also helped me proofread this post! Now, VS Code is my WordPress—a fast and accurate workflow for writing and optimizing content.

This GitHub Action ensures blog posts meet SEO standards and include relevant keywords, helping marketers and developers maintain quality directly within GitHub.

I invite you to install the Action, and if you’re a developer, consider contributing to the project.

## Release Notes: Content Linter GitHub Action v1.0.0

### Overview

Excited to announce the release of the Content Linter GitHub Action! This action is designed to help you ensure that your blog posts meet technical SEO requirements and include relevant keywords. It performs two main checks:

1. **Technical SEO**: Ensures that all titles, descriptions, and images exist and are described as needed. It also checks for broken links.
2. **Keywords**: Ensures that one or more of the declared keywords appear in relevant places. The declared keywords are stored in a configuration file called `keywords.txt`. 

Tip: Make sure you have it with your own keywords before using the script 

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
