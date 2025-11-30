from typing import Protocol

#interface or Protocol Assign
class TV(Protocol):
    def power(self)-> None:
        ...
#recallable method
def status(condition:TV):
    condition.power()

class On:
    def __init__(self , name:str):
        self.name = name

    def power(self) -> None:
        print(f"{self.name} TV Currently on screen!!!")

class Off:
    def __init__(self,brand:str):
        self.brand = brand

    def power(self) -> None:
        print(f"{self.brand} TV Currently screen Off")

if __name__ == "__main__":
    on = On("SAMSUNG")
    off = Off("Nokia")

    status(on)
    status(off)