#!/usr/bin/python3
""" recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], a=""):
    """recursive function that queries the Reddit API and returns a
    list containing the titles"""

    headers = {'User-Agent': 'MyPythonScript/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={a}'
    request = requests.get(url=url, headers=headers, allow_redirects=False)
    if request.status_code != 200:
        return None
    else:
        hot_list.extend(list_titles(
            request.json().get('data').get('children')))
        a = request.json().get('data').get('after')
        if a is None:
            return hot_list
        return recurse(subreddit, hot_list, a)


def list_titles(hot_list, titles=[]):
    """list titles of hot posts"""
    if len(hot_list) == 0:
        return titles
    else:
        titles.append(hot_list[0].get('data').get('title'))
        return list_titles(hot_list[1:], titles)
