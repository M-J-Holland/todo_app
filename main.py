# Todoapp
message = "Enter 'add', 'edit', 'complete' or 'quit'"
todos = []

while True:
    #get user input
    user_input = input(f"{message}: ").lower().strip()
    if user_input == 'add' or user_input.startswith('a'):
        todo = input("Enter a todo to add: ")
        todos.append(todo)