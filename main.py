import uvicorn 
from fastapi import FastAPI 
from slowapi.errors import RateLimitExceeded
from fastapi.middleware.cors import CORSMiddleware
from api_server import router
# Port for the model
PORT = 8000

app = FastAPI(
    title="SLOP", 
    description="Syllabus Logic & Optimized Planning"
)

# This is to ensure Rate Limitation 
app.include_router(router)
app.add_exception_handler(RateLimitExceeded)

# CORS configuration 
app.add_middleware(
    CORSMiddleware,
        allow_origins=['*'], 
        allow_credentials=True, 
        allow_methods=['*'], 
        allow_headers=['*']
)

if __name__ == "__main__":
    # Making the endpoint work
    uvicorn.run(
        app,
        host="0.0.0.0", 
        port=PORT,
    )

    