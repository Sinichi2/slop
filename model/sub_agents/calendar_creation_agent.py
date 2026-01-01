from pydantic import BaseModel, Field
from typing import List
import json 
class CalendarEvent(BaseModel):
    summary: str = Field(description="The title of the event")
    start_time: str = Field(description="Start time in ISO format")
    end_time: str = Field(description="End time in ISO format")
    location: str = Field(None, description="Physical or virtual location")

class CalendarExtraction(BaseModel): 
    events: List[CalendarEvent]

# Function

with open('../context_engineering/calendar_creation_agent.json', 'r') as f: 
    context=json.load(f)
