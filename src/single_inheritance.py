class Parent:

    def give_food(self):
        return "Mother giving Food"

    def give_money(self):
        return "Father giving Money"


class Child(Parent):

    def crying_bady(self):
        return "Baby is Crying and want to eat Food"

baby = Child()
print(baby.crying_bady())

print(baby.give_money())
print(baby.give_food())