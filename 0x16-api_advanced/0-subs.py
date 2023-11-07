#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """get number of subscribers"""

    request = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")
    if request.status_code == 200:
        return request.json().get("subscribers")
    return 0
