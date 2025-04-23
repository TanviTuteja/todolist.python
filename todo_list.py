todo_list = []

def show_task():
    print("\n your todo list:")
    if not todo_list:
        print("No tasks yet")
    else:
        for index, task in enumerate(todo_list, start =1): 
            print(f" {index}, {task}") 

def add_task():
    task = input("Enter New Task:")
    todo_list.append(task)
    print(f'"{task}" added to the list')


while True:

    print("\n--- To do List Menu ---")
    print("1. show task")
    print("2 add_task")
    print("3 Exit")

    choice = input("Choose your option (1-4)").strip()

    if choice == '1':
     show_task()

    elif choice == '2':
     add_task()

    elif choice == '3':
      print("Goodbye")
      break
  
    else:
     print("Invalid Choice..Try again Later")







