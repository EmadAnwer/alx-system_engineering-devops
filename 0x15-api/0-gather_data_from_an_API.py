#!/usr/bin/python3
"""gather data from API"""

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
    emp_name = employee_data.get('name')

    # get all Tasks for all employees
    tasks_list = requests.get(f'{URL}/todos').json()

    n_tasks = 0
    n_done_tasks = 0
    todo_tasks_list = []
    for task in tasks_list:
        if task.get('userId') == user_ID:
            n_tasks += 1
            if task.get('completed'):
                n_done_tasks += 1
                todo_tasks_list.append(task.get('title'))

    print(f"Employee {emp_name} is done with tasks({n_done_tasks}/{n_tasks}):")
    for task in todo_tasks_list:
        print(f"\t {task}")
