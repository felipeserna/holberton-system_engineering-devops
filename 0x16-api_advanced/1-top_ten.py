#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
If not a valid subreddit, print None
"""

import requests


def top_ten(subreddit):
    """top ten posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    my_header = {"User-Agent": "user_agent"}
    response = requests.get(url, headers=my_header, allow_redirects=False)

    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))

    else:
        print("None")
