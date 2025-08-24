# Content Linter

A linter for Markdown blog posts based on [Why Content Linting Matters: QA for the GenAI Era](https://www.vcsaga.com/blog/2025-08-05-content-linting-matters).
It checks for technical SEO, keyword usage, link health, headings, images, spelling, and readability.
The linter can run locally as a CLI tool or inside GitHub Actions.

## CLI Usage

```bash
pip install .
content-linter --posts-dir _posts --keywords-file .github/scripts/keywords.txt
```

The command exits with a non-zero status if any check fails, including spelling and readability.

## GitHub Action

```yaml
- uses: razkpp/content-linter@v0
  with:
    keywords-file: .github/scripts/keywords.txt
```

## Release Notes

### v.0.1
- Initial release of the Content Linter GitHub Action.
- Technical SEO validation: Checks for titles, descriptions, and images.
- Keyword validation: Ensures relevant keywords are present.
- Spell check: Detects and corrects spelling errors.
- Easy integration with GitHub workflows.

### v.0.2
- Added recommendations for internal and external links.
- Added recommendations for including at least one image.
- Improved error and warning messages.

## 👋 Hey, I'm Raz

I'm a hands-on, data-driven marketer with **8+ years in early-stage startups**, blending strategy with execution. I help technical founders build and scale their **go-to-market (GTM) foundations**, making them **growth-ready** through a mix of **modern marketing, AI-powered automation, and data-driven insights**.

### 🏗 What I Do (Modern Marketing)
I run a boutique GTM service tailored for B2B startups beyond stealth mode. I specialize in:
- **GTM Strategy & Execution** – From zero to a scalable marketing engine
- **Marketing Infrastructure** – Tools, automation, and AI-powered workflows
- **Competitor & Market Analysis** – Data-backed insights for positioning and growth
- **Content & Messaging Frameworks** – PLG, partner-led, founder-led, or outbound growth

---
### 📫 Get in Touch
- **[LinkedIn](https://www.linkedin.com/in/razkaplan/)**
- **[Blog](https://razkaplan.vercel.app/)**

## Fun Projects I built with the help of AI tools:
- [Hebrew Wordle for kids](https://base44.app/apps-show/-2fc96a8e)

🚀 Let's talk if you're a **B2B startup founder** looking to build a scalable marketing foundation!
