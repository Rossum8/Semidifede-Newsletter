# Semidifede Weekly Newsletter

An automated, AI-driven newsletter pipeline using GitHub Actions, Gemini API, and Substack.

## How It Works

1. **Planner (`planner.md`)**: Update this file whenever you want to set a theme or specify instructions for the upcoming week.
2. **Raw Notes (`raw/`)**: Drop any text files, notes, or excerpts into this folder during the week. The AI reads them.
3. **RSS Feeds (`sources.json`)**: Add URLs to trusted Catholic blogs. The AI will pull the latest 3 articles from each.
4. **Automation**: Every Thursday at 08:00 UTC (or manually via the Actions tab), GitHub Actions runs `main.py`.
5. **Output**: A highly-formatted markdown file is created in `drafts/`. Copy the text, paste it into Substack, and send!

## Setup Instructions

1. **Get a Gemini API Key**: Go to Google AI Studio, sign in with your Google account, and create a free API Key.
2. **Set up GitHub Secrets**:
   - Go to your repository **Settings** > **Secrets and variables** > **Actions**.
   - Click **New repository secret**.
   - Name: `GEMINI_API_KEY`
   - Secret: *[Paste your API key here]*
3. **GitHub Pages (Landing Page)**:
   - Go to **Settings** > **Pages**.
   - Under **Build and deployment**, set the Source to **Deploy from a branch** and select `main`.
   - Your SEO-optimized landing page will be published!
4. **Substack Integration**:
   - Open `index.html`.
   - Replace the `src` URL in the `<iframe>` with your actual Substack embed URL.

---

## 🔁 How to Transfer Ownership to Another Google Account

Since you are not the permanent owner of this project, here is how you seamlessly hand it over:

### 1. Transfer the GitHub Repository
1. Go to repository **Settings** > **General**.
2. Scroll to the very bottom to the **Danger Zone**.
3. Click **Transfer ownership**.
4. Type the GitHub username of the new owner. They will receive an email to accept the transfer.

### 2. Update the Gemini API Key
The current API key is linked to your Google account. To detach your account:
1. Have the **new owner** log in to [Google AI Studio](https://aistudio.google.com/) with *their* Google account and generate a new API Key.
2. The new owner must go to the repository **Settings** > **Secrets and variables** > **Actions**.
3. Update the `GEMINI_API_KEY` secret with their new key.
4. You can then delete your original API key from your Google AI Studio dashboard.

### 3. Update the Substack (If applicable)
If you created the Substack under your email:
1. Log into Substack.
2. Go to Settings > Team.
3. Invite the new owner as an Admin/Publisher.
4. Once they accept, they can remove your account from the publication.

*By following these steps, your Google account will be completely detached from the project, and it will be 100% owned by the new user.*
