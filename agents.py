from crewai import Agent
from tools import youtube_channel_tool
from dotenv import load_dotenv
load_dotenv()

import os

os.environ["OPENAI_API_KEY"]= os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini"

# Initialize an LLM instance to pass to Agents. Adjust the model name via
# the OPENAI_MODEL_NAME environment variable or change the default below.
from crewai.llm import LLM
llm = LLM(model="gpt-4o-mini")

## create a senior blog content researcher 
blog_researcher=Agent(
    role='Blog Researcher from youtube videos',
    goal='Search and find the most relevant videos about {topic} from Krish Naik YouTube channel (@krishnaik06)',
    name='blog_researcher',
    verbose=True,
    memory=False,  # Disabled to reduce API calls
    backstory=(
        "Expert in understanding videos in AI Data science, Machine learning and GEN AI and providing suggestions. "
        "You search for videos from Krish Naik's channel by using queries like 'site:youtube.com/@krishnaik06 [topic]'"
    ),
    tools=[youtube_channel_tool],
    llm = llm,
    allow_delegation=True,
)

## create a senior blog writer agent with YT tool
blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT channel',
    verbose=True,
    memory=False,  # Disabled to reduce API calls
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[youtube_channel_tool],
    llm = llm,
    allow_delegation=False
)
