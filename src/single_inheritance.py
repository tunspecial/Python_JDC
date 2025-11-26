class Parent:

    def __init__(self , foot_name:str , amount:int):
        self.foot_name = foot_name
        self.amount = amount

    def give_food(self):
        return f"Mother giving {self.foot_name}"

    def give_money(self):
        return f"Father giving {self.amount} kyats "

class Child(Parent):

    def crying_bady(self):
        return "Baby is Crying and want to eat Food"

baby = Child("banana" , 100)
print(baby.crying_bady())

print(baby.give_money())
print(baby.give_food())