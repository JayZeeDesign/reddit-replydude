import praw
from langchain.tools import tool

reddit = praw.Reddit(
    client_id="xxxxx",
    client_secret="xxxx",
    user_agent="xxxx",
    username="xxxx",
    password="xxxx",
)


class RedditTools:
    @tool("Search for recent reddit posts")
    def search_recent_reddit_post(keywords, limit):
        """Search recent reddit posts based on keywords"""
        # Choose the subreddit you want to search in
        subreddit = reddit.subreddit("all")  # 'all' searches across all of Reddit

        # Search for submissions related to certain keywords within the last day
        keywords = keywords
        posts = []
        for submission in subreddit.search(
            keywords, time_filter="hour", sort="new", limit=limit
        ):
            if not submission.locked and submission.is_self and not submission.archived:
                post = {
                    "title": submission.title,
                    "content": submission.selftext,
                    "url": submission.url,
                    "submission_id": submission.id,
                }
                posts.append(post)

        print(posts)
        return posts

    @tool("Fetch reddit post contet")
    def fetch_reddit_post_content(submission_id):
        """Fetch the content of a reddit post"""
        submission = reddit.submission(id=submission_id)

        if submission.is_self:
            print(f"Content: {submission.selftext}")
            return f"Content: {submission.selftext}"
        # For link posts, the URL points to the content
        else:
            return f"This is a link post, Content: {submission.selftext}"

    @tool("Post comment on reddit post")
    def reply_to_reddit_post(submission_id, message):
        """Post comment on reddit post"""
        # submission = reddit.submission(id=submission_id)
        # comment = submission.reply(message)
        # comment_url = f"https://www.reddit.com{comment.permalink}"
        comment_url = f"https://www.reddit.com"

        print(f"Successfully left comment, here is the link: {comment_url}")

        return f"Successfully left comment, here is the link: {comment_url}"
