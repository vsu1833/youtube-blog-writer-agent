# YouTube Blog Writer Agent

An AI-powered blog writing system that researches YouTube videos and creates comprehensive blog posts using CrewAI.

## Features

- Searches for relevant YouTube videos from specified channels
- Extracts key information from video content
- Generates well-structured blog posts automatically
- Uses multiple AI agents working together (researcher + writer)

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Serper API key (for web search)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/vsu1833/youtube-blog-writer-agent.git
cd youtube-blog-writer-agent
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key from https://platform.openai.com
   - Add your Serper API key from https://serper.dev (free tier available)

## Usage

Run the crew:

```bash
python crew.py
```

The system will:

1. Search for videos about the specified topic
2. Research and analyze the content
3. Generate a blog post saved as `new-blog-post.md`

## Configuration

Edit `crew.py` to change the topic:

```python
result = crew.kickoff(inputs={'topic': 'Your Topic Here'})
```

## Project Structure

- `agents.py` - Defines AI agents (researcher and writer)
- `tasks.py` - Defines tasks for each agent
- `tools.py` - Configures tools (web search)
- `crew.py` - Main execution file
- `.env` - Environment variables (not committed to git)

## License

MIT

## Notes

- Make sure you have sufficient OpenAI API credits
- The free Serper tier provides 2,500 searches/month
- Memory and cache are disabled to reduce API costs
