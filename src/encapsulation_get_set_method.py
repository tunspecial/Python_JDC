class StudentValidate:
    def __init__(self , name:str , id:int):
        self.name  = name
        self.__id = self.__validate_id(id)

    def __validate_id(self , id:int):
        if id >= 0 :
            return id
        else:
            print("ID must be positive Number")
            return 0

    @property
    def check_id(self):
        return self.__id

    @check_id.setter
    def check_id(self , actual_id:int):
        if actual_id >= 0:
            print(f"OK you are valid student {self.name}")
            self.__id = actual_id
        else:
            print("You are not valid student")

check1 = StudentValidate("ko ko" , 10)
check2 = StudentValidate("mg mg" , -10)
print(check1.check_id)
print(check2.check_id)