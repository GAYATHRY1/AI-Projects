from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("Bookkeeping MCP")

# 🔢 Mock transaction data
dummy_transactions = [
    {"amount": 1200.00, "category": "sales", "date": "2025-07-01", "notes": "July invoice"},
    {"amount": -300.00, "category": "utilities", "date": "2025-07-03", "notes": "Electricity bill"},
    {"amount": -150.00, "category": "supplies", "date": "2025-07-05", "notes": "Office stationery"},
    {"amount": 800.00, "category": "sales", "date": "2025-07-07", "notes": "Client payment"},
]

dummy_reminders = []

# 🧾 Tool 1: Log a transaction
@mcp.tool()
def log_transaction(amount: float, category: str, date: str, notes: str = "") -> str:
    """Logs an income or expense transaction"""
    dummy_transactions.append({
        "amount": amount,
        "category": category,
        "date": date,
        "notes": notes
    })
    return f"Transaction logged: ${amount} - {category} on {date}"

# 💵 Tool 2: Generate profit/loss summary
@mcp.tool()
def generate_summary(period: str = "monthly") -> str:
    """Generates a financial summary from dummy data"""
    income = sum(t["amount"] for t in dummy_transactions if t["amount"] > 0)
    expenses = sum(-t["amount"] for t in dummy_transactions if t["amount"] < 0)
    net = income - expenses
    return (
        f"📅 Summary ({period}):\n"
        f"- Income: ${income:.2f}\n"
        f"- Expenses: ${expenses:.2f}\n"
        f"- Net Profit: ${net:.2f}"
    )

# 📆 Tool 3: Create billing reminder
@mcp.tool()
def create_billing_reminder(client_name: str, amount_due: float, due_date: str) -> str:
    """Creates a dummy reminder for billing"""
    reminder = {
        "client": client_name,
        "amount_due": amount_due,
        "due_date": due_date
    }
    dummy_reminders.append(reminder)
    return f"Reminder created: {client_name} owes ${amount_due} by {due_date}"

# 🪪 Resource: Greeting
@mcp.resource("bookkeeping/greeting://{name}")
def bookkeeping_greeting(name: str) -> str:
    return f"Hello {name}, welcome to your Bookkeeping MCP dashboard. 💼"

# 🧠 Prompt: Tax tips by country
@mcp.prompt()
def tax_report_tips(country: str = "Italy") -> str:
    templates = {
        "Italy": "Outline deductible categories and quarterly VAT filing best practices in Italy.",
        "USA": "Summarize common Schedule C deductions and 1099 reporting tips for small businesses.",
        "UK": "Explain allowable expenses and HMRC self-assessment requirements.",
      "India": "Highlight GST filing timelines, applicable thresholds, and common business deductions under Indian tax law."      
    }
    return templates.get(country, f"Share general tax guidance for businesses operating in {country}.")

# 🏁 Run the MCP server
if __name__ == "__main__":
    mcp.run(transport="stdio")
