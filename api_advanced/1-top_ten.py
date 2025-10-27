#!/usr/bin/python3
"""
1-top_ten.py

This module defines a function `top_ten(subreddit)` that queries the Reddit API
and prints the titles of the first 10 hot posts listed for a given subreddit.

If the subreddit is invalid or does not exist, it prints None.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python:api_advanced:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
    except requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        print(None)
        return

    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
