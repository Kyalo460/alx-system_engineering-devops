#!/usr/bin/python3
"""A function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers)
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subs."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-agent": "Linux:0x16-advanced_api"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
