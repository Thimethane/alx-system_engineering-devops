#!/usr/bin/python3

import json
import requests


def fetch_user_data(user_id):
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        return None

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get('username')

    tasks_list = []
    for task in todos_data:
        task_dict = {
            "username": username,
            "task": task.get('title'),
            "completed": task.get('completed'),
        }
        tasks_list.append(task_dict)

    return {user_id: tasks_list}


def main():
    all_users_data = {}

    # Assuming the user IDs range from 1 to 10, adjust the range accordingly
    for user_id in range(1, 11):
        user_data = fetch_user_data(user_id)

        if user_data:
            all_users_data.update(user_data)

    # Write to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_users_data, json_file, indent=2)


if __name__ == "__main__":
    main()
