from crewai import Crew, Process
from file_io import save_markdown

from agents import RedditAgents
from tasks import RedditTasks
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

OpenAIGPT4 = ChatOpenAI(model="gpt-4")

agents = RedditAgents()
tasks = RedditTasks()

things_to_promote = """"
AI youtube channel(https://www.youtube.com/channel/UCrXSVX9a1mj8l0CMLwKgMVw), below is 3 of most recent videos that we want to plug, make sure you include youtube url in the comment:
1. How to build an AI sales agent that can outreach prospect, cold call them and follow up on whatsapp
2. How to reduce Large language model cost for your AI applications (When developing AI applications, LLM model is a big cost, and ability to reduce LLM cost is critical for ai startups, here we discussed 6 ways to reduce cost)
3. How to build universal web scraper to scraping website with AI Agents
"""

# Setting up agents
reddit_post_finder = agents.reddit_post_finder()
reddit_comment_writer = agents.reddit_comment_writer()
reddit_comment_poster = agents.reddit_comment_poster()

# Setting up tasks
search_recent_reddit_post_task = tasks.search_recent_reddit_post_task(
    reddit_post_finder, things_to_promote
)
draft_reddit_comment = tasks.draft_reddit_comment(
    reddit_comment_writer, [search_recent_reddit_post_task]
)
post_reddit_comment = tasks.post_reddit_comment(
    reddit_comment_poster, [draft_reddit_comment]
)

# Setting up tools
crew = Crew(
    agents=[reddit_post_finder, reddit_comment_writer, reddit_comment_poster],
    tasks=[search_recent_reddit_post_task, draft_reddit_comment, post_reddit_comment],
    process=Process.hierarchical,
    manager_llm=OpenAIGPT4,
)


results = crew.kickoff()

print(results)
