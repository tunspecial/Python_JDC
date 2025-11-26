class Employee:
    def __init__(self , name , emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"ID : {self.emp_id} , Name : {self.name}"

class Developer(Employee):
    def write_code(self):
        return f"{self.name} writing code!!!"

    def solve_problem(self):
        return "Analyzing and solving technical issues!! "

class Manager(Employee):
    def manage_team(self):
        return f"{self.name} is managing the team!!"

    def solve_problem(self):
        return "Negotiating and solving personnel issues."

class TeamLead(Developer):
    def review_code(self):
        return f"{self.name} is reviewing code and architecture!!"

class Director(TeamLead , Manager):
    def __init__(self , name , emp_id , stock_options):
        super().__init__(name , emp_id)
        self.stock_options = stock_options

    def set_strategy(self):
        team_mgmt = self.manage_team()
        return f"Setting company strategy and granting {self.stock_options} stock options. | {team_mgmt}"

if __name__ == "__main__":
    director = Director(name="Tun Tun" , emp_id=61 , stock_options=5000)

    print(f"Details: {director.get_details()}")

    print(director.review_code())

    print(director.set_strategy())
