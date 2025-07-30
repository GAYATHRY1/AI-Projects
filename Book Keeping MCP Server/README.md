# Bookkeeping-MCP-Server

AI-powered toolset for small business finance tracking and automation

## 📌 Overview

This project is a custom-built Model Context Protocol (MCP) server designed to help small business owners manage transactions, billing, tax summaries, and cash flow insights. It integrates with Claude Desktop and exposes tools via FastMCP.

## 🚀 Features

| Tool Name              | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| log_transaction        | Records income or expense with category, date, and notes                    |
| generate_summary       | Calculates profit/loss from dummy data                                      |
| create_billing_reminder| Sets reminders for client payments                                          |
| bookkeeping_greeting   | Personalized greeting for financial dashboard access                        |
| tax_report_tips        | Generates country-specific tax advice using Claude prompts                  |

## 🛠️ Setup Instructions

### 1. Install Prerequisites

```bash
pip install uv
```

## 2. Initialize Project
```bash
uv init bookkeeping-mcp-server
cd bookkeeping-mcp-server
uv add "mcp[cli]"
```
## 3. Create main.py
## 4. Install Server into Claude Desktop
```bash
uv run mcp install main.py
```
## 5. Restart Claude Desktop
Use Task Manager to close Claude Desktop completely, then relaunch.

## 📺 Demo: Claude Chat Result
👉 Coming soon: demo video showing transaction logging and summary generation

## 💡 Future Enhancements
Connect to Google Sheets for real-time data storage

Add invoice generation and PDF export

Integrate with Stripe or PayPal for payment tracking

Implement authentication via Google OAuth

