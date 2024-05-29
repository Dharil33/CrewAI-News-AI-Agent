from crewai import Crew,Process
from tasks import researcher_task,write_task
from agents import news_researcher,news_writer

crew = Crew(
    agents=[news_researcher,news_writer],
    tasks=[researcher_task,write_task],
    process=Process.sequential
)

result = crew.kickoff(inputs={'topic':'Loksabha election 2024 in India'})
print(result)