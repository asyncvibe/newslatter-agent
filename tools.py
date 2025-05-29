from dotenv import load_dotenv
load_dotenv()
import os
from crewai_tools import SerperDevTool
# setup the tool for internet searching capabilities
google_search_tool = SerperDevTool(
    serper_api_key=os.getenv("SERPER_API_KEY"))