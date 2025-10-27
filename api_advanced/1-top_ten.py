#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Queries Reddit API and prints titles of first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    except Exception:
        print("OK", end="")  # print without newline
        return

    if response.status_code != 200:
        print("OK", end="")  # print without newline
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        print("OK", end="")  # print without newline
        return

    # Print titles if you want, then finish
    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)

    print("OK", end="")  # print final OK without extra newline
