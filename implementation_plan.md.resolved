# Semidifede Weekly - Automated Newsletter Architecture Plan

This plan outlines the architecture and workflow to build a fully automated, AI-driven newsletter for "semidifede", modeled after the ASSIST Weekly approach. The goal is to maximize automation while keeping the entire stack **100% free**, optimizing for **Google Search ranking (SEO)**, and scaling to a large audience.

## Core Decisions (Updated)

1. **Email Platform for Large Audiences**: **Substack**.
   - *Why?* Since your wife has 15k Instagram followers, she could easily get 1,000+ newsletter subscribers on day one. Every other platform (Brevo, Mailchimp, MailerLite) will charge you heavily once you pass 1,000 subscribers or 300 emails/day. 
   - **Substack is 100% free for unlimited subscribers.** They only take a fee if you start charging readers for paid subscriptions. It also has the absolute best SEO for past issues.
   - *The Catch*: Substack does not have an official API. Therefore, our automation will generate the final formatted newsletter as a file, and she will just need to spend 1 minute copy-pasting it into Substack and clicking send.
2. **The "Brain" & Automation**: **GitHub Actions** (100% Free). A scheduled workflow will run our Python script automatically once a week.
3. **Landing Page**: **GitHub Pages** (100% Free). We will build a lightning-fast, SEO-optimized static HTML/CSS landing page to collect emails and redirect signups to the Substack.
4. **Data Sources**: 
   - A `raw/` folder for custom content/notes.
   - A list of trusted Catholic blogs and RSS feeds.
   - **NEW: A `planner.md` document**.

---

## Proposed Architecture & Workflow

### 1. The GitHub Repository (The Workspace)
We will create a GitHub repository. It will contain:
- **`planner.md`**: Your wife can randomly update this with ideal scheduled topics, seasonal themes (e.g., Lent, Advent), or specific ideas.
- **`raw/` folder**: Drop any original text, catechism excerpts, or notes here throughout the week.
- **`sources.json`**: A list of URLs for trusted blogs/RSS feeds.
- The Python automation script and the Landing Page code.

### 2. Data Ingestion & AI Processing (GitHub Actions + Gemini)
Every Thursday (or your preferred day), GitHub Actions will wake up and run the script:
1. **Context Gathering**: The script reads `planner.md` to identify the current theme/goals. It reads everything in the `raw/` folder, and fetches the latest articles from the trusted blogs.
2. **Gemini AI**: The script sends all this context to the free Gemini API. Gemini acts as the "Semidifede Editor".
3. **Curation & Gap Filling**: Gemini looks at the `planner.md` instructions. It tailors the gathered content to fit the plan. If the plan has gaps, Gemini will autonomously generate relevant Catholic content or use the latest news/blogs to fill the gaps.
4. **Draft Generation**: Gemini filters, scores, categorizes, and writes the plain-English summaries, outputting a highly formatted Markdown file.

### 3. Review & Distribution (The Manual Step)
- **The Output**: The script will save the finished newsletter as `drafts/latest_issue.md` in the repository.
- **Notification**: GitHub Actions can send you an email saying: *"The Semidifede draft is ready"*.
- **Action**: You or your wife open the markdown file, copy the text, paste it into Substack, do a final review, and hit "Send". 

### 4. SEO-Optimized Landing Page (GitHub Pages)
We will build a custom landing page (like ASSIST Weekly) instead of just using Substack's default page.
- **SEO Best Practices**: Proper `<title>`, `<meta name="description">`, semantic tags, and optimized performance to ensure Google ranks it highly.
- **Form Integration**: An embedded Substack signup iframe, so users can subscribe directly from your beautiful custom page.

---

> [!IMPORTANT]
> ## User Review Required
> Please confirm this updated plan. Once approved, I will begin execution by:
> 1. Setting up the project folder structure (including the `planner.md` and `raw/` folder).
> 2. Writing the core Python script for Data Ingestion and Gemini AI processing.
> 3. Designing the SEO-optimized Landing Page.
