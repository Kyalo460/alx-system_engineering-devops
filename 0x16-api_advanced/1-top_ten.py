#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """Returns the top 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0-subs.py/1.0"
        }
    params = {
        "limit": 10
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if (response.status_code == 404):
        print("None")
        return

    results = response.json().get("data")

    [print(c.get("data").get("title")) for c in results.get("children")]

    