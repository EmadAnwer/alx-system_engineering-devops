#!/usr/bin/python3
"""gather data from API save to csv"""

import csv
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
    for task in tasks_list:
        if task.get('userId') == user_ID:
            employee_tasks_list.append(task)

    with open(f'{user_ID}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        # "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
        for task in employee_tasks_list:
            writer.writerow([f"{user_ID}",
                             f"{username}",
                             f"{task.get('completed')}",
                             f"{task.get('title')}"])
