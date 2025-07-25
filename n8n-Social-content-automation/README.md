# 🧠 Social Media Content Automation with n8n

This repo documents a no-code automation workflow built in n8n to generate and publish content to LinkedIn and Medium using free AI models.

## 📌 Workflow Overview

<img width="1497" height="789" alt="Screenshot 2025-07-16 173543" src="https://github.com/user-attachments/assets/97b123aa-1741-48e1-ad9c-85ea2e5c4c99" />

### 🔗 Inputs
- Google Sheets with fields:
  `Content Topic`, `Target Audience`, `PostType`, etc.

### 🤖 AI Agent
- Google Gemini Flash 2.0 (free-tier)
- Generates LinkedIn-style posts

### 📣 Publishing
- LinkedIn via OAuth2
- Medium via import or RapidAPI workaround

### 💾 Backup
- Manual export of workflow as JSON
- Stored in `/workflow.json`

## 📂 Files
- `workflow.json`: Full n8n workflow
- `/images/`: Screenshots and visual references

## 🧠 Sticky Notes Summary

> ✨ Automate post creation from a Google Sheet  
> ✨ Enrich content using Tavily and AI  
> ✨ Publish to LinkedIn and Medium  
> ✨ Track status back in the Sheet  
> ✨ Built entirely with free-tier tools

---

## ⚙️ Setup Instructions

1. Clone this repository
2. Import `workflow.json` into your n8n dashboard
3. Add your credentials:
   - Google Sheets OAuth2
   - Tavily API Key
   - Gemini Flash 2.0 API Key
   - LinkedIn OAuth2
4. Customize your prompt and sheet fields
5. Hit ✨“Execute workflow”✨ to generate content

---

## 📌 Limitations

- OpenAI and DeepSeek may block requests without quota—use fallback models
- Medium API tokens no longer available for new users—use import workaround
- Designed for single-user publishing; multi-profile logic can be added

---

## 📣 Coming Soon (Ideas)

- Auto-translate posts before publishing 🌐  
- Schedule publishing via n8n Cron node 🕒  
- Slack/Telegram alerts on publishing 🎯  
- Repurpose content for Instagram Threads 🧵  
