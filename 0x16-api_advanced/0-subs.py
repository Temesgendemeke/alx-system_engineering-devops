#!/usr/bin/python3
import requests
"""return number of subreddit subscribers"""


def number_of_subscribers(subreddit):
    """
    _summary_

    Args:
        subreddit (_type_): _description_

    Returns:
        _type_: _description_
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    res = response.json()
    return res['data']['subscribers']
