#!/usr/bin/python3
"""_summary_"""


if __name__ == "__main__":
    from sys import argv
    import requests
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
            print("Employee {} is done with tasks({}/{}):"
                  .format(user['name'], done, total))
            for value in values:
                if value['userId'] == id and value['completed']:
                    print("\t {}".format(value['title']))
