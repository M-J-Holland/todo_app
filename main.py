# Todoapp
import os

message = "Enter 'add', 'show', 'edit', 'complete' or 'quit'"


def read_todos():
    if os.path.exists("todos.txt"):
        with open("todos.txt", "r") as file:
            return file.readlines()
    return []


def write_todos(local_todos):
    with open("todos.txt", "w") as file:
        file.writelines(local_todos)


while True:
    # get user input
    user_input = input(f"{message}: ").lower().strip()

    # Add feature
    if user_input == 'add' or user_input.startswith('ad'):
        todos = read_todos()
        while True:
            if not todos:
                todo = input("Enter a todo to add, type 'done' when you are finished: ").strip() + "\n"
            else:
                todo = input("Enter another todo, type 'done' when you are finished: ").strip() + "\n"
            if todo.strip().lower() == 'done':
                write_todos(todos)
                break
            todos.append(todo)


    # Show feature
    elif user_input == "show" or user_input.startswith('sh'):
        todos = read_todos()
        if not todos:
            print("No todos to show, add some first them come back to see them.")
            continue
        else:
            for index, todo in enumerate(todos, start=1):
                print(f"{index}. {todo.strip()}")

    # Edit feature
    elif user_input == 'edit' or user_input.startswith('ed'):
        todos = read_todos()
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
                todos[todo_to_edit] = edited_todo + "\n"
                write_todos(todos)
        else:
            print("Invalid todo number, please try again.")

    # Complete feature
    elif user_input == 'complete' or user_input.startswith('com'):
        todos = read_todos()
        if not todos:
            print("No todos to complete, add some first them come back to complete them.")
            continue
        todo_to_complete = input("Enter the number for the todo you would like to complete: ")
        if todo_to_complete.isdigit():
            todo_to_complete = int(todo_to_complete) - 1
            if todo_to_complete < 0 or todo_to_complete >= len(todos):
                print("Invalid todo number, please try again.")
                continue
            else:
                todos.pop(todo_to_complete)
                write_todos(todos)

        else:
            print("Invalid todo number, please try again.")

    # Quit feature
    elif user_input == 'quit' or user_input.startswith('q'):
        print("Goodbye!")
        break

    else:
        print("Invalid input, please try again.")
