#!/usr/bin/python3
"""return number of subreddit subscribers"""


import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers

    Args:
        subreddit (string): name of subreddit

    Returns:
        nubmer : number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    res = response.json()
    return res['data']['subscribers']
