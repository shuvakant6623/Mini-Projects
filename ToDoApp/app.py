def task():
    tasks = [] 
    print("-------WELCOME TO THE TASK MANAGEMENT APP-------")
    Total_tasks = int(input("Enter how many tasks you want to add"))
    for i in range(0, Total_tasks):
        task = input(f"Enter task {i+1} :")
        tasks.append(task)
    print(f"Todays tasks are \n {tasks}")

    while True:
        try:
            operation = int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
            if operation == 1:
                new_task = input("Enter task:")
                tasks.append(new_task)
                print(f"Task {new_task} has been added successfully.")
            elif operation == 2:
                updated_task = input("Enter the task you want to update")
                if updated_task in tasks:
                    update = input("Enter new task:")
                    ind = tasks.index(updated_task)
                    ind[tasks] = update
                    print(f"Task {update} has been updated successfully")
                else:
                    print("Task not found")
            elif operation == 3:
                del_task = input("Enter the task you want to delete:")
                if del_task in tasks:
                    ind = tasks.index(del_task)
                    del tasks[ind]
                    print(f"Task {del_task} has been deleted successfully.")
                else:
                    print("Task not found")
            elif operation == 4:
                print(f"Total tasks = {tasks}")
            elif operation == 5:
                print("Closing the program.....")
                break
            else:
                print("Invalid input. Please enter a number from 1 to 5.")
        except ValueError as e:
            print("Invalid input. Please enter a valid number.")

task()