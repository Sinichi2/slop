from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from config import Config
import orchestrator, json

config = Config()

# Initializing Orchestrator
orchestrator_agent = create_agent(
    ChatGoogleGenerativeAI(
        model=config.GEMINI_MODEL, 
        api_key=config.GEMINI_API_KEY, 
        project=config.PROJECT_ID
    )
)

# 