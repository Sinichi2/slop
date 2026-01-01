import pytest
from pydantic import ValidationError
import sys
import os

# Add the model directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../model')))

from sub_agents.calendar_creation_agent import CalendarEvent, CalendarExtraction

def test_calendar_event_validation():
    """Test valid and invalid calendar event data."""
    valid_event = {
        "summary": "Meeting",
        "start_time": "2023-10-27T10:00:00Z",
        "end_time": "2023-10-27T11:00:00Z",
        "location": "Online"
    }
    event = CalendarEvent(**valid_event)
    assert event.summary == "Meeting"
    
    invalid_event = {
        "summary": "Meeting"
        # missing start_time and end_time
    }
    with pytest.raises(ValidationError):
        CalendarEvent(**invalid_event)

def test_calendar_extraction_validation():
    """Test calendar extraction model."""
    data = {
        "events": [
            {
                "summary": "Event 1",
                "start_time": "2023-10-27T10:00:00Z",
                "end_time": "2023-10-27T11:00:00Z"
            }
        ]
    }
    extraction = CalendarExtraction(**data)
    assert len(extraction.events) == 1
    assert extraction.events[0].summary == "Event 1"

