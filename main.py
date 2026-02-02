# Todoapp
message = "Enter 'add', 'edit', 'complete' or 'quit'"
todos = []

while True:
    #get user input
    user_input = input(f"{message}: ").lower().strip()

    # Add feature
    if user_input == 'add' or user_input.startswith('a'):
        todo = input("Enter a todo to add: ")
        todos.append(todo)
    # Show feature
    elif user_input == "show":
        if not todos:
            print("No todos to show, add some first them come back to see them.")

        else:
            for index, todo in enumerate(todos, start=1):
                print(f"{index}. {todo}")