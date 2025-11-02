welcome = """
========================
TODO Application
========================
"""
operation = """
Select Operation
1.Show task
2.Create task
3.Find task
4.Delete task
"""

thanks = """
========================
Thank You!!!
========================
"""

if __name__ == "__main__":
    print(welcome,end="")
    id = 0
    tasks:dict[int,str] = {}
    while True:
        print(operation)
        
        operation_id = input("Select ID : ")
        
        match operation_id :
            case "1":
                print("Task List")
                print("====================")
                if len(tasks) > 0:
                    for key in tasks.keys():
                        print(f"{key} : {tasks.get(key)}")
                else:
                    print("There is not task")
                print("====================",end="")
            case "2":
                print("Create Task")
                print("====================")
                id +=1
                task_name = input("Task Name : ")
                tasks[id] = task_name ##tasks[101] → "Buy groceries"
                print(f"Your task is create at id : {id} ")
                print("====================",end="")
            case "3":
                print("Find Task")
                print("====================")
                keyword = input("Search Keyword : ")
                found = False
                for id in tasks.keys():
                    task = tasks[id] ## tasks[101] → "Buy groceries"
                    if task.lower().startswith(keyword.lower()):
                        print(f"{id} : {task}")
                        found = True
                if not found:
                    print("There is not result")
                print("====================",end="")
            case "4":
                print("Delete Task")
                print("====================")
                task_id = input("Task ID : ")
                task = tasks.get(int(task_id))
                if task == None:
                    print(f"There is no task with id {task_id}")
                else:
                    del tasks[int(task_id)]
                    print("Your task is deleted")
                print("====================",end="")
            case _:
                if operation_id == "Exit":
                    break                  
                else:
                    print(f"Please Enter Operation ID Number : ")
                      
    print(thanks)