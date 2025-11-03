id = 0
tasks:dict[int,str] = {}

def operation(name:str):
    def decorator(func):# func parameter - decorate လုပ်မယ့် original function
        def warapper(*args , **kwargs): # Innder Function
            print(name)
            print("------------------------")
            func(*args, **kwargs) ##original function မှာ ရှိနိုင်တဲ့ arguments အားလုံးကို receive လုပ်တယ်
            print("------------------------")
        return warapper
    return decorator

@operation("Task List")
def show_all():
    if len(tasks) > 0 :
        for key in tasks.keys():
            print(f"{key}.{tasks.get(key)}")
            
    else:
        print("There is no tasks")

@operation("Create_task")
def create_task():
    while True:
        task_name = input("Task Name : ")
        if task_name == "":
            print("Task name cannot be empty!\n")
        else:
            global id ## Global scope မှာရှိတဲ့ id variable ကို modify လုပ်ဖို့ declare လုပ်တယ်
            id += 1 
            tasks[id] = task_name
            print(f"Your Task is create with : {id}")
            break

@operation("Find Task")
def find_task():
    keyword = input("Search Keyword : ")
    found = False
    for id in tasks.keys():
        task = tasks[id]
        if keyword.lower() in task.lower(): #Example: "python" ဆိုရင် "Learn Python", "Python Tutorial", "Advanced Python" အားလုံးတွေ့မယ်
            print(f"{id}.{task}")
            found = True
    if not found:
        print("There is no result")
          
@operation("Delete Task") 
def delete_task():
    task_id = input("Task ID : ")
    task = tasks.get(int(task_id))
    if task == "":
        print(f"There is no task with id {task_id}")
    else:
        del tasks[int(task_id)]
        print("Your task is deleted")
        


