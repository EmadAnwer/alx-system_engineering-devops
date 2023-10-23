#!/usr/bin/python3
"""gather data from API save to csv"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    try:
        user_ID = int(argv[1])
    except Exception as a:
        exit()

    URL = 'https://jsonplaceholder.typicode.com'
    # get employee name
    employee_data = requests.get(f'{URL}/users/{user_ID}').json()
    if employee_data == {}:
        exit()
    username = employee_data.get('username')

    # get all Tasks for all employees
    tasks_list = requests.get(f'{URL}/todos').json()

    employee_tasks_list = []
    user_task_dict = {}

    for task in tasks_list:
        if task.get('userId') == user_ID:
            employee_tasks_list.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username,
            })
    user_task_dict[f"{user_ID}"] = employee_tasks_list
    with open(f"{user_ID}.json", "w") as outfile:
        json.dump(user_task_dict, outfile)
