# Avinash_decodelabs_task1
 # To-Do-list

 ### Brief One Line Summary
A simple, command-line interface (CLI) application written in Python to add and view daily tasks.

 ### Overview
This project is a minimal, console-based task management tool designed to help users keep track of their immediate to-do items. It runs in a continuous loop, allowing users to interactively manage a basic list dynamically in memory.

 ### Problem Statement
People often need a quick, distraction-free way to log and view tasks without relying on heavy GUI applications or cloud-based software. This tool provides a lightweight, local alternative for basic task tracking.

 ### Tools and Technologies
* **Language:** Python 3
* **Concepts Used:** Infinite loops (`while True`), conditional branching (`if-elif-else`), list manipulation (`.append()`), and string formatting.

 ### Methods
* **Task Storage:** Utilizes a globally declared Python list (`tasks = []`) to hold tasks dynamically in memory.
* **Control Flow:** Implements a standard `while` loop paired with `input()` evaluation to drive the interactive CLI menu.
* **Enumeration:** Uses Python's built-in `enumerate()` function to dynamically index and number the tasks when displaying them to the user.

 ### How to Run this project?
1. Ensure you have Python installed on your system.
2. Copy the project code into a file named `TODO_LIST.py`.
3. Open your terminal or command prompt and navigate to the directory containing the file.
4. Run the script using the following command:
   ```bash
   python TODO_LIST.py
   
 ### Results & Conclusion
* The script successfully fulfills the basic requirements of an interactive, terminal-based to-do application. It handles incorrect menu choices gracefully and effectively keeps track of inputs during its runtime.

  
 ### Future Work
* Data Persistence: Implement file handling (e.g., saving to a .txt or .json file) so tasks aren't lost when the program exits.

* Task Deletion: Add a feature to remove or mark tasks as completed.

* Task Prioritization: Introduce due dates or priority tags for better task organization.

 ### Dashboard/Model/Output
The application uses a plain-text terminal interface. 

```text
1. Add Task
2. View Tasks
3. Exit
Select option (1/2/3): 1
Enter task: Buy groceries
'Buy groceries' added!

1. Add Task
2. View Tasks
3. Exit
Select option (1/2/3): 2

--- Your To-Do List ---
1. Buy groceries
