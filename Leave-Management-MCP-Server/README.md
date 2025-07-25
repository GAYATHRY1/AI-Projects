# Leave-Management-MCP-Server
AI-powered toolset for HR leave tracking and automation

## 📌 Overview

This project is a custom-built Model Context Protocol (MCP) server designed to help HR teams manage employee leave requests, balances, and policy explanations. It integrates with Claude Desktop and exposes tools via FastMCP.

## 🚀 Features
## Tool Name	Description
1. check_leave_balance -	Returns remaining vacation and sick days for a given employee
2. submit_leave_request-	Submits a leave request with type, duration, and reason
3. hr_greeting  -	Personalized greeting for HR dashboard access
4. explain_leave_policy	- Generates country-specific leave policy summaries using Claude prompts

## 🛠️ Setup Instructions

## 1. Install Prerequisites

pip install uv 

## 2. Initialize Project

uv init my-first-mcp-server

cd my-first-mcp-server

uv add "mcp[cli]"

## 3. Create main.py


## 4. Install Server into Claude Desktop

uv run mcp install main.py

## 5. Restart Claude Desktop
Use Task Manager to kill any running instance, then relaunch.

## 📺 Demo: Claude Chat Result

👉 [Click here to watch demo video](demo.mp4)


## 💡 Future Enhancements

1. Add approval workflows
2. Integrate with calendar APIs
3. Store leave history in a database

## 🙌 Credits
Built using FastMCP, Claude Desktop, and insights from the Codebasics community.

Special thanks to Codebasics for the inspiration, tutorials, and hands-on guidance that made this MCP project possible
For Reference: https://www.youtube.com/watch?v=jLM6n4mdRuA&t=38s
Github Link: https://github.com/codebasics/ai-agents/tree/main/2_mcp_leave_management
