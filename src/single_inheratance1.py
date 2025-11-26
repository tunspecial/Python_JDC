class Employee:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self , name:str , salary:int):
        self.name = name
        self.salary = salary
        self.extra_bonus = 0.10

    def bonus_calculation(self):
        return  self.salary * self.extra_bonus

    def get_info(self):
        return f"Employee Name | {self.name} | Salary | {self.salary}"

class Manager(Employee):
    def __init__(self , name:str , salary:int , department:str):
        super().__init__(name, salary)
        self.department = department
        self.manager_extra_bonus = 0.05
    """
        Method Overriding: 
        Calculates manager bonus by adding their rate to the employee bonus.
    """
    def bonus_calculation(self):
        base_bonus = super().bonus_calculation()
        manager_bonus = self.salary * self.manager_extra_bonus
        return  base_bonus + manager_bonus

    def get_info(self):
        person_info = super().get_info()
        return f"{person_info} | Department | {self.department}"

if __name__ == "__main__":

    Emp1 = Employee("Ko Ko" ,50000)
    print(Emp1.get_info())
    print(f"Ko Ko's Bonus {Emp1.bonus_calculation():,.2f}")
    print("_" * 40)

    Emp2 = Employee("Min Min" ,100000)
    print(Emp2.get_info())
    print(f"Min Min's Bonus {Emp2.bonus_calculation():,.2f}")
    print("_" * 40)

    Mag1 = Manager("Maung Maung" , 80000 , "IT Department")
    print(Mag1.get_info())
    print(f"Maung Maung's Bonus : {Mag1.bonus_calculation():,.2f}")
    print("_" * 40)

    Mag2 = Manager("Zaw Zaw" , 150000 , "Sale Department")
    print(Mag2.get_info())
    print(f"Zaw Zaw 's Bonus : {Mag2.bonus_calculation():,.2f}")
    print("_" * 40)