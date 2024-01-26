# Task Manager Project

This project is a simple task manager that retrieves tasks for multiple employees from a fake API and exports the data in JSON format.

## Requirements

- Python 3.x
- Requests library (install it using `pip install requests`)

## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/task-manager.git
    ```

2. Navigate to the project directory:

    ```bash
    cd task-manager
    ```

3. Run the script:

    ```bash
    python3 task_manager.py
    ```

4. Check the generated JSON file:

    ```bash
    cat todo_all_employees.json
    ```

## Notes

- The script fetches task data for users with IDs ranging from 1 to 10 (adjust the range as needed).
- Each user's tasks are stored in a dictionary with the user ID as the key.
- The data is exported to a JSON file named `todo_all_employees.json`.

Feel free to modify the script or adapt it to your specific needs.

