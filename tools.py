from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv
import os
load_dotenv()
from main import ser_api_key

# Initialize the tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()