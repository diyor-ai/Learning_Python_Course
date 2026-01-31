todos = ["Reading Book", "Cleaning House", "Cook the Dinner"]

while True:
    print("\n1. Add")
    print("2. Remove")
    print("3. View")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_task = input("Enter new task: ")
        todos.append(new_task)
        print("Task added.")

    elif choice == "2":
        if not todos:
            print("Todo list is empty.")
            continue

        for i, task in enumerate(todos):
            print(i, task)

        index = int(input("Enter index to delete: "))

        if 0 <= index < len(todos):
            todos.pop(index)
            print("Task removed.")
        else:
            print("Invalid index.")

    elif choice == "3":
        if not todos:
            print("No tasks.")
        else:
            for i, task in enumerate(todos):
                print(i, task)

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")
