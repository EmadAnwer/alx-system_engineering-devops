#!/usr/bin/python3
"""gather data from API save to json"""

import json
import requests


if __name__ == "__main__":

    URL = 'https://jsonplaceholder.typicode.com'
    # get all users
    users_list = requests.get(f'{URL}/users').json()
    # get all Tasks for all employees
    tasks_list = requests.get(f'{URL}/todos').json()
    todo_all_employees = {}
    for user in users_list:
        user_id = user.get('id')
        employee_tasks_list = []
        for task in tasks_list:
            if task.get('userId') == user_id:
                employee_tasks_list.append({
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                })

        todo_all_employees[user_id] = employee_tasks_list

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(todo_all_employees, outfile)
