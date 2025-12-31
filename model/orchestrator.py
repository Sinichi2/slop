"""
    This agent will conduct a hand-off to two other agents, which will be the 
    sub-agents: 
        - Calendar creation agent 
        - Calendar designer agent
"""

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph import StateGraph, START, END, MessageState
from config import Config
from fastmcp import FastMCP
import json

config = Config()


# Initializing StateGraph
class State(StateGraph): 
    pass

#Loading the json file
with open("context_engineering/orchestrator.json", "r") as f:
    context=json.load(f)

# Initializing Orchestrator
aggregator_agent = create_agent(
    ChatGoogleGenerativeAI(
        model=config.GEMINI_MODEL, 
        api_key=config.GEMINI_API_KEY, 
        project=config.PROJECT_ID
    )
)

# 
async def orchestrator_agent(): 
    pass