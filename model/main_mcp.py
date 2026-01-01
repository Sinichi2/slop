from fastmcp import FastMCP
from tools import transfer_to_creation_agent
from dataclasses import dataclass
from typing import List

# Initializing the FastMCP to initialize
mcp = FastMCP("calendar agents")

@dataclass
class context_schema: 
    current_user: str

# Initializing the mcp 
@mcp.tool(name="calendar creation agent", description="This tool allows the orchestrator agent to handoff to it's sub_agent: calendar_creation")
def ics_creation(
        events: List[dict], 
        file_name: str, 
    ) -> str: 
    transfer_to_creation_agent()