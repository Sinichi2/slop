from typing import Literal
from typing_extensions import NotRequired
from langchain.agents import create_agent, AgentState
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command
from langchain.tools import tool, ToolRuntime # Fixed casing
from langchain.messages import ToolMessage
import json

#Loading the json file
with open("context_engineering/orchestrator.json", "r") as f:
    context=json.load(f)

# 1. Consistent State Schema
class OrchestratorState(AgentState): 
    active_agent: NotRequired[str]
    # current_step can be used for middleware routing if needed

# 2. Handoff Tool
@tool 
def transfer_to_creation_agent(runtime: ToolRuntime) -> Command: 
    """Transfer the user to the calendar_creation_specialist."""

    last_ai_msg = runtime.state["messages"][-1]

    # Fixed typo: tool_call_id
    transfer_msg = ToolMessage(
        content="Transferring to calendar creation specialist...", 
        tool_call_id=runtime.tool_call_id 
    )

    return Command(
        goto="calendar_agent", 
        update={
            "active_agent": "calendar_agent", 
            # Crucial: Include both messages to keep history valid
            "messages": [last_ai_msg, transfer_msg]
        }
    )

# 3. Agent Initialization
# Note: In production, load MCP tools once outside the node to avoid latency
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
orchestrator_runnable = create_agent(
    model=llm,
    tools=[transfer_to_creation_agent],
    system_prompt=context
)

# 4. Correct Node Function
async def orchestrator_node(state: OrchestratorState): 
    # Nodes in LangGraph must return a dictionary or a Command
    response = await orchestrator_runnable.ainvoke(state)
    return response

# 5. Graph Construction
builder = StateGraph(OrchestratorState)
builder.add_node("orchestrator", orchestrator_node)
builder.add_node("calendar_agent", calendar_creation_node) # Define this node

builder.add_edge(START, "orchestrator")
graph = builder.compile()