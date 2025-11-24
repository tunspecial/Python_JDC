from pydantic import BaseModel
# Name Mangling
class BankAccount:
    def __init__(self , amount:int):
        self.__amount = amount

    def show_amount(self):
        return f"Current Your amount -> {self.__amount}"

ower = BankAccount(1000)
print(ower.show_amount())

ower._BankAccount__amount = 2000
print(ower.show_amount())
##############################################################
# Internal (Protected) only
class Person:
    def __init__(self , name:str , age:int) -> None:
        self._name = name
        self._age = age

    def person_inf0(self):
        return f"Your name is  {self._name} and {self._age} year olds!!"

p = Person("tun tun" , 32)
print(p.person_inf0())

p._age = 1
p._name = "ko ko"
print(p.person_inf0())

################################################################
class Student(BaseModel):
    name : str
    age : int

    class CondigDict:
        frozen = True

s = Student(name="Maung Maung" , age=40)
print(s)

s.name = "Ko Ko"
print(s)