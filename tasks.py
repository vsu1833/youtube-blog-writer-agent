from crewai import Task
from tools import youtube_channel_tool
from agents import blog_writer, blog_researcher

## Research Task
research_task = Task(
    description=(
        "Search for videos about {topic} from Krish Naik's YouTube channel (@krishnaik06). "
        "Use search queries like 'site:youtube.com/@krishnaik06 {topic}' to find relevant videos. "
        "Identify the most relevant video and gather key information about the content."
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
    tools=[youtube_channel_tool],
    agent=blog_researcher,
)

# Writing task with language model configuration
write_task = Task(           
    description=(
        "Using the research findings, create a comprehensive blog post about {topic}. "
        "Write in an engaging, educational style that makes complex topics accessible."
    ),
    expected_output='A well-structured blog post summarizing the video content on {topic} with clear explanations and insights',
    tools=[youtube_channel_tool],
    agent=blog_writer,
    async_execution=False,  # if set to true then both of the agents will be working in parallel
    output_file='new-blog-post.md'   # Example of output customization
)
