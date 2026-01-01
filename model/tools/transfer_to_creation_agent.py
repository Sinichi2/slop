from typing import List, Optional
from dataclasses import dataclass
from ics import Calendar, Event 
from datetime import datetime
import os

@dataclass
class context_schema: 
    current_user: str

def ics_creation(
        events: List[dict], 
        file_name: Optional[str] = None, 
    ) -> str: 
    """ Create an .ics file """ 

    # Calendar  
    c = Calendar()
    # Events
    for e in events: 
        event = Event()
        event.add('summary', e['title'])
        event.add('dstart', datetime.datetime.fromisoformat(e['start_time']))
        event.add('dtend', datetime.datetime.fromisoformat(e['end_time']))
        if e.get('location'): 
            event.add('location', e['location'])
        c.add_component(event)    
    
    # Filename Logic: Use provided name or default
    if file_name and file_name.strip():
        # Strip the original extension (e.g., .pdf, .docx) and add .ics
        base_name = os.path.splitext(file_name)[0]
        filename = f"{base_name}.ics"
    else:
        filename = "your_schedule.ics"

    with open(filename, 'wb') as f:
        f.write(c.to_ical())
    return f"Successfully generated {filename}"