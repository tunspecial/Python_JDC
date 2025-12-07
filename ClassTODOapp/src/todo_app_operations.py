from enum import Enum
from src.interface import Operation , Application

class Task:
    class Status(Enum):
        Create = "0"
        Done = "1"
        Cancel = "2"

    _current_id = 0

    def __init__(self , name:str)-> None:
        self.__class__._current_id += 1
        self.id = self.__class__._current_id
        self.name = name
        self.status = Task.Status.Create

class TaskManager:
    _instance:TaskManager | None = None

    def __new__(cls,) -> TaskManager:
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        self._tasks:dict[int , Task] = {}

    def create_task(self , name:str) -> Task:
        task = Task(name=name)
        self._tasks[task.id] = task
        return task

    def get_all(self)-> list[Task]:
        return list(self._tasks.values())

    def find_by_id(self , ids:int) -> Task | None :
        return self._tasks.get(ids)

    #delete task id or if not found
    def delete_task(self , ids:int) -> Task | None:
        return self._tasks.pop(ids , None)

class TaskBaseOperation:
    def __init__(self)-> None:
        self._manager = TaskManager()

class ShowAllTask(TaskBaseOperation , Operation):
    def __init__(self , ids = 1) -> None:
        super().__init__()
        self.ids = ids
        self.name = "Show All Task"

    def do_business(self):
        task_list = self._manager.get_all()
        if len(task_list) > 0:
            print(f"{'':-<46}")
            print(f"{"ID":<4} {"Name":<30} {"Status":<12}")
            print(f"{'' :-<46}")
            for task in task_list:
                print(f"{task.id:<4} {task.name:<30} {task.status.name:<12}")
            print(f"{'':-<46}")
        else:
            print("There is No Data!!!")

class CreateTask(TaskBaseOperation , Operation):
    def __init__(self , ids = 2 ) -> None:
        super().__init__()
        self.ids = ids
        self.name = "Create Task"

    def do_business(self):
        task_name = input("Enter Task Name : ")
        task = self._manager.create_task(task_name)
        print(f"{task.name} is created with id {task.id}...")

class UpdateStatus(TaskBaseOperation , Operation):
    def __init__(self , ids = 3) -> None:
        super().__init__()
        self.ids = ids
        self.name = "Update Status"

    def do_business(self):
        #get task id
        task_id = input("Enter Task ID : ")

        task = self._manager.find_by_id(int(task_id))
        if task is None:
            print(f"There is No Task With {task_id}")
            return
        if task.status != Task.Status.Create:
            print(f"{task.status.name} can not be Update!")
            return
        print("Select Status")
        print("1. Done")
        print("2. Cancel")
        selected_value = input("Status ID : ")
        task.status = Task.Status(selected_value)
        print(f"{task.name} status is updated to {task.status.name}!")

class UpdateTaskName(TaskBaseOperation , Operation):
    def __init__(self , ids = 4) -> None:
        super().__init__()
        self.ids = ids
        self.name = "Update Task Name"

    def do_business(self):
        #get task id
        task_id = input("Enter Task ID : ")
        #find task
        task = self._manager.find_by_id(int(task_id))
        # check if the take exists
        if task is None:
            print(f"There is No Task ID {task_id}")
            return
        #store before take name
        before_task_name = task.name
        #get new task name
        new_task_name = input(f"Enter New Task Name (Current Task Name is : {before_task_name}): ")
        #no empty new task name
        if not new_task_name:
            print("Task Name Can Not Empty!!!")
            return
        #update task name
        task.name = new_task_name
        print(f"\nTask ID ({task_id}) Task Name had been updated with {new_task_name}")

class DeleteTask(TaskBaseOperation , Operation):
    def __init__(self , ids = 5) -> None:
        super().__init__()
        self.ids = ids
        self.name = "Delete Task"

    def do_business(self):
        # get task id
        task_id = input("Enter Task ID : ")
        #to delete task
        deleted_task = self._manager.delete_task(int(task_id))
        #if result is None
        if deleted_task is None:
            print(f"There is no task with id {task_id}")
        else:
           print(f"Your task ID {task_id} is ({deleted_task.name}) is deleted")

if __name__ == "__main__":
    operation = [
        CreateTask(ids = 1),
        ShowAllTask(ids= 2),
        UpdateStatus(ids= 3),
        UpdateTaskName(ids = 4),
        DeleteTask(ids= 5)
    ]
    Application("TODO Application" , operation).start()
