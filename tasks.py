from datetime import datetime
from crewai import Task


class RedditTasks:
    def search_recent_reddit_post_task(self, agent, things_to_promote):
        return Task(
            description=f"""THINGS WE WANT TO PROMOTE & PLUG:
            ```{things_to_promote}```

            GOAL:
            Find 2 most relevant reddit posts where we can provide value & plug the things we want to promote
            """,
            agent=agent,
            async_execution=True,
            expected_output="""A list of top 2 most relevant Reddit posts regarding a certain topic. 
                Example Output: 
                [
                    {  'title': 'AI takes spotlight in Super Bowl commercials', 
                    'url': 'https://reddit.com/post1', 
                    'submission_id': '1bd3tac',
                    'reasoning': 'This post is relevant because it discusses the use of AI in advertising...'
                    }, 
                    ...
                ]
            """,
        )

    def draft_reddit_comment(self, agent, context):
        return Task(
            description="Draft a comment on a Reddit post",
            agent=agent,
            context=context,
            async_execution=True,
            expected_output="A drafted comment for the post, as well as submission_id",
        )

    def post_reddit_comment(self, agent, context):
        return Task(
            description="Post the comment generated from draft_reddit_comment on the Reddit post",
            agent=agent,
            context=context,
            expected_output="The URL of the comment that was posted on the Reddit post.",
        )
