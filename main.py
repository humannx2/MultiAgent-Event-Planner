import warnings
warnings.filterwarnings('ignore')

from agents import marketing_communications_agent,venue_coordinator,logistics_manager
from tasks import venue_task,marketing_task, logistics_task
from tools import search_tool, scrape_tool
from dotenv import load_dotenv
from crewai import Crew
import json
from pprint import pprint
import os
load_dotenv()


event_management_crew = Crew(
    agents=[venue_coordinator, 
            logistics_manager, 
            marketing_communications_agent],
    
    tasks=[venue_task, 
           logistics_task, 
           marketing_task],
    
    verbose=True
)

event_details = {
    'event_topic': "Tech Innovation Conference",
    'event_description': "A gathering of tech innovators "
                         "and industry leaders "
                         "to explore future technologies.",
    'event_city': "Bengaluru, India",
    'tentative_date': "2025-12-15",
    'expected_participants': 500,
    'budget': 2000000,
    'venue_type': "Conference Hall"
}

try:
    result = event_management_crew.kickoff(inputs=event_details)
    with open('venue_details.json') as f:
        data = json.load(f)
        pprint(data)
    # print(result)
except Exception as e:
    print(f"Error during execution: {e}")

