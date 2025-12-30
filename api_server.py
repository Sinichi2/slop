from fastapi import APIRouter
from pydantic import BaseModel
from slowapi import Limiter
from typing import Optional

# APIRouter
router = APIRouter()
# Rate Limiting
limiter = Limiter()

