#!/usr/bin/python3
"""
Gather data from an API
Export to JSON
"""


import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        api = "https://jsonplaceholder.typicode.com"
        user_id = sys.argv[1]

        data = requests.get("{}/users/{}".format(api, user_id)).json()
        todos = requests.get("{}/users/{}/todos".format(api, user_id)).json()
        tasks = []

        file_name = "{}.json".format(user_id)

        for task in todos:
            to_dict = {}
            to_dict["task"] = task.get("title")
            to_dict["completed"] = task.get("completed")
            to_dict["username"] = data.get("username")
            tasks.append(to_dict)
        full_dict = {user_id: tasks}

        with open(file_name, mode="w") as employee_file:
            json.dump(full_dict, employee_file)
