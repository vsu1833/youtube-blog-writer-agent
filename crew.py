from crewai import Crew,Process
from agents import blog_writer,blog_researcher
from tasks import write_task,research_task

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,   # Optional: Sequential task execution is default
    memory=False,  # Disabled to reduce API calls
    cache=False,   # Disabled to reduce API calls
    max_rpm=100,
    share_crew=False
)
## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'crewAI Crash Course For Beginners-How To Create Multi AI Agent For Complex Usecases'})
print(result)