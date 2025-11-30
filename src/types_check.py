from typing import Protocol

class WaterMachine(Protocol):
    def product(self)-> None:
        ...

def working(item:WaterMachine):
    item.product()

class Design:
    def __init__(self , name:str):
        self.name = name

    def product(self)-> None:
        print(f"{self.name} is Drawing Design")

class Packet:
    def __init__(self , size:int):
        self.size = size

    def product(self) -> None:
        print(f"{self.size} Liter size is Producing from Machine")

d = Design("Mung Mung")
p = Packet(4)

working(d)
working(p)
