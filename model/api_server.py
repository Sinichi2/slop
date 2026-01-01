from fastapi import APIRouter
from pydantic import BaseModel
from slowapi import Limiter
from typing import Optional
from orchestrator import orchestrator_agent

# APIRouter
router = APIRouter()
# Rate Limiting
limiter = Limiter()

# Request chat class
class ChatRequest(BaseModel): 
    prompt: str
    screenshot: Optional[str] = None
    document: Optional[str] = None

#Response class
class ChatResponse(BaseModel): 
    response: str
    image_output: Optional[str] = None

# Implemented a rate limiter to reduce spam: 3 messages per minute 
@limiter("3/minutes")
@router.post("/", response_model=ChatResponse)
async def chat(request:ChatRequest): 
    try:
        # This process the image output 
        response_text = await orchestrator_agent(request.prompt)
        # This will contain the image, keeping this none because this is optional 
        response_data = None
        # Will generate a response once the output is returned
        return ChatResponse(
            response = response_text, 
            image_output=response_data
        )
    # Error handling
    except Exception as e: 
        print(f"Error happened due to {e}")
        return ChatResponse(
            # No image generation
            response = f"Cannot process this request due to {e}"
        )
