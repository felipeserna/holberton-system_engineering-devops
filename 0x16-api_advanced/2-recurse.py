#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
If no results are found, return None
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """list of titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    my_header = {"User-Agent": "user_agent"}
    response = requests.get(url,
                            headers=my_header,
                            allow_redirects=False,
                            params={'after': after})

    if response.status_code == 200:
        after = response.json().get("data").get("after")
        if (after is None):
            return hot_list
        for post in response.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        return recurse(subreddit, hot_list, after)

    return None
