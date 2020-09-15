#!/usr/bin/python3
"""
Gather data from an API
Dictionary of list of dictionaries
"""


import json
import requests


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(api)).json()
    todos = requests.get("{}/todos".format(api)).json()
    file_name = "todo_all_employees.json"
    full_dict = {}

    for user in users:
        tasks = []
        for task in todos:
            if user.get('id') == task.get('userId'):
                to_dict = {}
                to_dict['task'] = task.get("title")
                to_dict['completed'] = task.get("completed")
                to_dict['username'] = user.get("username")
                tasks.append(to_dict)
        full_dict[user.get('id')] = tasks

    with open(file_name, mode='w') as employee_file:
        json.dump(full_dict, employee_file)
