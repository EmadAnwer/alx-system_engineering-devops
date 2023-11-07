#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """get number of subscribers"""

    headers = {'User-Agent': 'MyPythonScript/1.0'}
    request = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json", headers=headers)

    if request.status_code == 200:
        subscribers = request.json().get('data').get('subscribers')
        return subscribers if subscribers else 0
    return 0
