#!/usr/bin/python3
"""
How many subscribers for a given subreddit
Returns 0 if it is an invalid subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """How many subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    my_header = {"User-Agent": "user_agent"}
    response = requests.get(url, headers=my_header, allow_redirects=False)
    try:
        return response.json().get("data").get("subscribers")
    except Exception:
        return 0
