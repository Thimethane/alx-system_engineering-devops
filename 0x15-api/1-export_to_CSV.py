#!/usr/bin/python3
"""Python script that exports data in CSV format"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches employee information and their TODO list,
    then exports data to a CSV file.

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
        user_id = user_data.get("id")
        username = user_data.get("username")

        # Fetch TODO list for the given employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Create and write CSV file
        csv_filename = f"{user_id}.csv"
        with open(csv_filename, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

            # Write CSV records
            for todo in todos_data:
                task_completed_status = "True" if todo["completed"] else "False"
                csv_writer.writerow(
                    [user_id, username, task_completed_status, todo["title"]]
                )

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
