
tasks = []

def main():
    print("Welcome to DecodeLabs To-Do List Engine")

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Select option (1/2/3): ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print(f"'{task}' added!")

        elif choice == "2":
            if not tasks:
                print("List is empty!")
            else:
                print("\n--- Your To-Do List ---")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Please select 1, 2, or 3.")

main()