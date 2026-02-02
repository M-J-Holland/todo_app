# Todoapp
message = "Enter 'add', 'show', 'edit', 'complete' or 'quit'"
todos = []

while True:
    # get user input
    user_input = input(f"{message}: ").lower().strip()

    # Add feature
    if user_input == 'add' or user_input.startswith('a'):
        todo = input("Enter a todo to add: ")
        todos.append(todo)

    # Show feature
    elif user_input == "show" or user_input.startswith('s'):
        if not todos:
            print("No todos to show, add some first them come back to see them.")
            continue

        else:
            for index, todo in enumerate(todos, start=1):
                print(f"{index}. {todo}")

    # Edit feature
    elif user_input == 'edit' or user_input.startswith('e'):
        if not todos:
            print("No todos to edit, add some first them come back to edit them.")
            continue
        todo_to_edit = input("Enter the number for the todo you would like to edit: ")
        # checks to see if todo_to_edit is a valid number
        if todo_to_edit.isdigit():
            # Removes one from the number to stop listIndex errors
            todo_to_edit = int(todo_to_edit) - 1
            if todo_to_edit < 0 or todo_to_edit >= len(todos):
                print("Invalid todo number, please try again.")
                continue
            else:
                edited_todo = input("Enter your todo edit: ")
                todos[todo_to_edit] = edited_todo
        else:
            print("Invalid todo number, please try again.")