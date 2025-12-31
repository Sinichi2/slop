from dotenv import load_dotenv, find_dotenv
import os
# Initializing dotenv 
load_dotenv(find_dotenv(".env.model.dev"))

class Config: 
    GEMINI_API_KEY: str = os.getenv("GEMINI_API")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL")
    PROJECT_ID: str = os.getenv("PROJECT_ID")