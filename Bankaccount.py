# objective: model a bank account where the balance can only be changed through deposits and withdrawals, preventing direct modification.
# name of account holder and account number 
class Bankaccount():
    def __init__(self,name,account_number):
        self.name=name
        self.account_no=account_number
        self._balance=0
    
    def deposit(self,add_amount):
        self._balance+=add_amount
    
    def withdraw(self,take_amount):
        self._balance-=take_amount

    def view_balance(self):
        return f"name:{self.name}\naccount_number:{self.account_no}\nbalance:{self._balance}"
    

print("------welcome to go-to bank-------")
name=input("enter your name: ")
account_no=int(input("enter the account number: "))
coustmer=Bankaccount(name,account_no)
start=True
while start:
    print("if you want to deposit or withraw or check balance")
    choice=input()

    if choice=="deposit".lower():
        add_amount=input("enter the amount: ")
        coustmer.deposit(int(add_amount))
        print(coustmer.view_balance())
    elif choice=="withdraw".lower():
        withdraw_amount=input("enter the amount: ")
        coustmer.withdraw(int(withdraw_amount))
    elif choice=="check balance".lower():
        print(coustmer.view_balance())
    elif choice==" ":
        start=False
    else:
        print("none")




