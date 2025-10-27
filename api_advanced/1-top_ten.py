#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Queries Reddit API and prints titles of first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:alx:task1 (by /u/yourusername)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        if posts:
            for post in posts[:10]:
                print(post.get("data", {}).get("title"))
        else:
            print("None")
    else:
        print("None")
