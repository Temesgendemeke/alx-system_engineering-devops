#!/usr/bin/python3
"""_summary_"""


if __name__ == "__main__":
    import requests
    import json
    values = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    done = 0
    total = 0
    dump_dict = {}

    for value in values:
        if value['userId'] == id:
            total += 1
            if value['completed']:
                done += 1

    for user in users:
        id = user['id']
        dump_dict[id] = []
        if user['id'] == id and value['completed']:
            for value in values:
                dump_dict[id].append({"username": user['username'],
                                       "task": value['title'],
                                       "completed": value['completed']})
    with open("all.json", "a+") as jsonfile:
        json.dump(dump_dict, fp=jsonfile)
