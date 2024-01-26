#!/usr/bin/python3
"""Python script that fulfills the given requirements"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the progress of tasks for a given employee.

    Parameters:
    - employee_id (int): The ID of the employee.

    Returns:
    None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("name")

        # Fetch TODO list for the given employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Calculate the progress
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo["completed"])

        # Display the progress information
        print(
            f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}): "
        )
        # Display titles of completed tasks
        for todo in todos_data:
            if todo["completed"]:
                print(f"\t{todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
