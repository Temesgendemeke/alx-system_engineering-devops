#!/usr/bin/python3
"""_summary_"""


if __name__ == "__main__":
    import requests
    import json
    from sys import argv

    id = int(argv[1])
    values = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    done = 0
    total = 0

    for value in values:
        if value['userId'] == id:
            total += 1
            if value['completed']:
                done += 1

    for user in users:
        if user['id'] == id:
            with open("{}.json".format(id), "a+") as csvfile:
                for value in values:
                    if value['userId'] == id:
                        itr = {value['userId']: [
                               {"task": value['title'],
                                "completed": value['completed'],
                                "username": user['username']
                                }]}
                        json.dump(itr, fp=csvfile)
