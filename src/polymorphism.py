from typing import Protocol

class BankModule(Protocol):
    def bank_account(self , fromaccount : str , toaccount : str , amount : int)-> None:
        ...

class Bank:
    def __init__(self , banking:BankModule):
        self.banking = banking

    # recallable method
    def transfer(self , fromaccount:str , toaccount:str , amount:int):
        print("Transaction is Process ")
        self.banking.bank_account(fromaccount , toaccount , amount)
        print("Transaction is Finish ")

class Offline(BankModule):
    def bank_account(self, fromaccount: str, toaccount: str, amount: int):
        print(f"{amount} is transfer from {fromaccount} to {toaccount} via offline mode!!!")

class Online(BankModule):
    def bank_account(self , fromaccount : str , toaccount : str , amount : int) -> None:
        print(f"{amount} is transfer from {fromaccount} to {toaccount} via online mode!!!")

if __name__ == "__main__":
    offline = Bank(Offline())
    offline.transfer("Account A" , "Account B" , 1000)

    online = Bank(Online())
    online.transfer("From Ko Ko" , "From Mg Mg" , 10000)


