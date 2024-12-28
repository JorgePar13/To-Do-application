task = ["ADD", "VIEW", "DELETE", "QUIT THE APPLICATION"]
new_task = []
try:#the add command
    print(task)
    user_input = input("Hello, what would you like to do with your tasks today?")
    if user_input == (f"ADD"):
        add_task = (input("What task yould you like to add?"))
        new_task.append(add_task)
    elif user_input == (f"VIEW"):#the view command
        new_task == 0
        print("None")
    elif user_input == (f"DELETE"):#delete command
        del_task = input("What task would you like to delete? ")
        new_task == 0
        print("NO TASK TO DELETE")
    elif user_input == (f"QUIT"):#quit command
        print("SAVING PROGRESS....GOODBYE")
    else:
        print("Invalid option, please try again!")

finally:
    user_input = input("Is their any else you would like to do?")
    if user_input == (f"ADD"):#add command
        add_task = (input("What task yould you like to add?"))
        new_task.append(add_task)
    elif user_input == (f"VIEW"):#the view command after added task
        print(new_task)
    elif user_input == (f"DELETE"):#delete command after added task
        del_task = input("What task would you like to delete? ")
        del new_task[0]
        print("Task deleted")
        print(new_task)
    elif user_input == (f"QUIT"):#quit command
        print("SAVING PROGRESS....GOODBYE")
    else:
        print("Invalid option, please try again!")