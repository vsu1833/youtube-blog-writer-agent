from crewai_tools import SerperDevTool

# Using SerperDevTool instead of YoutubeChannelSearchTool due to pytube issues
# This tool can search the web including YouTube videos
# You'll need a SERPER_API_KEY in your .env file (get free key at serper.dev)
youtube_channel_tool = SerperDevTool()