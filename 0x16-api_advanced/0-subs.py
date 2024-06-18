#!/usr/bin/python3
"""A function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subs."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "0-subs.py/1.0"
        }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0

    result = response.json().get("data")

    if (result.get("subscribers") != None):
        return result.get("subscribers")
    else:
        return 0
