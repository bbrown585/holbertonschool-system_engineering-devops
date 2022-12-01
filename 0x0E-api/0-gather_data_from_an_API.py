#!/usr/bin/python3
"""A script that fetches the """

import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'

    user = requests.get(url + sys.argv[1])
    reqTodos = requests.get(url + sys.argv[1] + '/todos/')

    jsonemp = user.json()
    tasks = [key['completed'] for key in reqTodos.json()]
    print("Employee {} is done with tasks({}/{}):".format(jsonemp.get('name'),
          tasks.count(True), len(tasks)))
    for task in reqTodos.json():
        if task.get('completed') is True:
            print("\t {}".format(task.get('title')))
