User_prompt = "Enter the todo list:"

todos = []
while True:
    EnteredText = input("Enter the todo list:")
    # todo = EnteredText.capitalize()
    todo = EnteredText.title()
    todos.append(todo)
    print(todos)
