from crewai import Crew, Process
from tasks import research_task, writer_task, proofreader_task
from agents import researcher, writer, proofreader
from dotenv import load_dotenv
load_dotenv()
# creating crew
# try: 
crew = Crew(
        agents=[researcher, writer, proofreader],
        tasks=[research_task, writer_task, proofreader_task],
        process= Process.sequential, # to run tasks in sequence
    )

topic = "Artificial Intelligence in Finance"
# kicking off crew
result = crew.kickoff(inputs={"topic": topic})
print(result)
# except Exception as e:
#     print(f"Error: {e}")