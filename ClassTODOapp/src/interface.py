from abc import ABC , abstractmethod

class Operation(ABC):

    def __init__(self, ids:int, name:str) -> None:
            self.ids = ids
            self.name = name

    @abstractmethod
    def do_business(self):
        pass

    def execute(self):
            print(f"{self.ids}. {self.name}")
            self.do_business()
            print("\n")

_MESSAGE_FORMAT = """
==========================
{}
=========================="""

class Application:
    def __init__(self , name:str , operations:list[Operation])-> None:
        self.name = name
        self.operations = operations

    @staticmethod
    def show_message(message:str):
        print(_MESSAGE_FORMAT.format(message))

    def get_operation(self):
        print("Select Operation")
        for operation in self.operations:
            print(f"{operation.ids}. {operation.name}")

        selected_ids = input("\nSelect ID : ")

        for operation in self.operations:
            if operation.ids == int(selected_ids):
                return operation
        return None

    def start(self):
        Application.show_message(self.name)
        while True:
            operation = self.get_operation()
            if operation is None:
                break
            operation.execute()
        Application.show_message("Thank You!!!")