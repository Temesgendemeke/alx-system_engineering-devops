#!/usr/bin/python3
"""return number of subreddit subscribers"""


import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        res = response.json()
        i = 1
        
        for r in res['data']['children']:
            if i > 10:
                break
            i+=1
            print(r['data']['title'])
    else:
        return 0