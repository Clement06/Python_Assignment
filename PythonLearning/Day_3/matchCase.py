todos = []
while True:
    userAction = input("Type add, edit,complete or show list:")
    userAction = userAction.strip()
    match userAction:
        case 'show' | 'display':
            # print(todos)
            for index, item in enumerate(todos):
                # todos = item.title()
                row = f"{index+1}.{item.title()}"
                print(row)
                # print(index, '.', item.title())
        case 'add':
            todo = input("Enter a todo:")
            todo = todo.strip()
            todos.append(todo)
        case 'edit':
            number = int(input("Enter the number of Todo to edit:"))
            number = number - 1
            new_todo = input("Enter the new todo: ")
            print(new_todo)
            todos[number] = new_todo
        case 'complete':
            # print(todos)
            for item in todos:
                print(item)
            todo = input("Enter the item to complete:")
            # to remove the space in the input
            todo = todo.strip()
            todos.remove(todo-1)
        case 'exit':
            break
        case _:
            print("hey!, you have entered unknown option")
print("Byee")
