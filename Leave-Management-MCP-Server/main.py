from mcp.server.fastmcp import FastMCP
from typing import List

# In-memory mock databse with 20 leave days to start
employee_leaves = {
    "E001": {"balance":18, "history": ["2024-12-25" , "2025-01-01"]},
    "E002": {"balance": 20, "history": []}
}
# Create the MCP server
mcp = FastMCP("Leave Management MCP")


# Tool 1: Check leave balance
@mcp.tool()
def check_leave_balance(employee_id: str) -> str:
    """Returns leave balance info for an employee"""
    mock_data = {
        "EMP001": "10 vacation days, 3 sick days remaining",
        "EMP002": "5 vacation days, 1 sick day remaining",
        "EMP003": "Out of vacation days, 2 sick days remaining"
    }
    return mock_data.get(employee_id, "No leave data found for this employee.")


# Tool 2: Submit leave request
@mcp.tool()
def submit_leave_request(employee_id: str, type: str, days: int, reason: str) -> str:
    """Submits a leave request"""
    return (
        f"Leave request submitted for {employee_id}:\n"
        f"- Type: {type}\n"
        f"- Days: {days}\n"
        f"- Reason: {reason}"
    )


# Resource: Personalized HR message
@mcp.resource("leave/greeting://{name}")
def hr_greeting(name: str) -> str:
    """Returns a leave-related greeting"""
    return f"Hello {name}, your leave dashboard is ready."


# Prompt: Generate leave policy explanation
@mcp.prompt()
def explain_leave_policy(country: str = "India") -> str:
    """Prompt Claude to explain country-specific leave policies"""
    templates = {
        "India": "Summarize vacation, sick leave, and maternity leave laws applicable in India.",
        "USA": "Explain FMLA, vacation, and sick leave norms followed in the US.",
        "Germany": "Describe paid time off policies and sick leave rights in Germany.",
    }
    return templates.get(country, f"Give a general overview of leave policies in {country}.")

# Run server
if __name__ == "__main__":
    mcp.run(transport="stdio")
