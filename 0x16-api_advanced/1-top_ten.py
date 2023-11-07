#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """querie Reddit API and prints first 10 hot posts"""

    headers = {'User-Agent': 'MyPythonScript/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    request = requests.get(url=url, headers=headers, allow_redirects=False)
    if request.status_code == 200:
        hot_ten = request.json().get('data').get('children')
        if not hot_ten:
            return print("None")
        else:
            for child in hot_ten:
                print(child.get('data').get("title"))
    else:
        return print("None")
