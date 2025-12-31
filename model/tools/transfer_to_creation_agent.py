from fastmcp import FastMCP 
from langchain.tools import tool, ToolRuntime
from langgraph.types import Command
from typing import Literal

mcp = FastMCP("transfer_to_calendar_creation")

@mcp.tool()
@tool(name="transfer_to_creation_agent", description="This tool allows the orchestrator agent to handoff to it's sub_agent: calendar_creation")
def transfer_to_creation(runtime: ToolRuntime) -> Command: 
    """
        Transfer to the calendar creation agent
    """
    last_ai_message = next(
        msg for msg in reversed(runtime.state[""])
    )
    
