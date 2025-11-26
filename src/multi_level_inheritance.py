class Vehicle:
    def __init__(self , brand , year):
        self.brand = brand
        self.year = year
        print(f"---{self.brand} Vehicle created!!!--------")

    def start_engine(self):
        return "start engine ready to move!!"

class Car(Vehicle):
    def __init__(self , brand , year , door):
        super().__init__(brand, year)
        self.door = door

    def door_open(self):
        return f"Car Door Open (total door : {self.door})"

    def drive(self):
        return "Car is Driving on the Road"

class ElectricCar(Car):
    def __init__(self , brand , year , door , battery_range):
        super().__init__(brand , year , door)
        self.battery_range = battery_range

    def charge(self):
        return f"{self.brand}. Est Range {self.battery_range} km"

    def start_engine(self):
        return "Electric motor activated. Silent Start"

if __name__ == "__main__":
    tesla = ElectricCar("Tesla Model 3" , year=2025 , door=4 , battery_range=400)
    print("------Calling Method--------")
    print(f"Vehicle Year: {tesla.year}")
    print(tesla.start_engine())

    print(tesla.door_open())
    print(tesla.drive())

    print(tesla.charge())
