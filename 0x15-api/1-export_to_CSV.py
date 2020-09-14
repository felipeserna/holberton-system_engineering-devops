#!/usr/bin/python3
"""
Gather data from an API
Export to CSV
"""


import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        api = "https://jsonplaceholder.typicode.com"
        user_id = sys.argv[1]

        data = requests.get("{}/users/{}".format(api, user_id)).json()
        todos = requests.get("{}/users/{}/todos".format(api, user_id)).json()
        done = 0
        total = len(todos)
        tasks = []

        for task in todos:
            if task.get("completed") is True:
                done = done + 1
                tasks.append("\t " + task.get("title"))

        print("Employee {} is done with tasks({}/{}):".
              format(data.get("name"), done, total))
        print("\n".join(tasks))

        file_name = "{}.csv".format(user_id)

        with open(file_name, mode="w") as employee_file:
            writer = csv.writer(employee_file, quoting=csv.QUOTE_ALL)
            name = data.get("username")

            for task in todos:
                writer.writerow([user_id,
                                 name,
                                 task.get("completed"),
                                 task.get("title")])
