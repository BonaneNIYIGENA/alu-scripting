#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Queries Reddit API and prints titles of first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Python:api_advanced:v1.0 (by /u/yourusername)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    except requests.RequestException:
        print(None)
        return

    # If subreddit is invalid or redirect occurs, print None
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
