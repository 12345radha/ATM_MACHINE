class Atm:
    def __init__(self) -> None:
        self.__pin=""
        self.__balance=0

        self.menu()
    
    def __menu(self):
        user_input=input("""
                        Hello,how would you like to proceed?
                         1.Enter 1 to create pin
                         2.Enter 2 to deposit
                         3.Enter 3 to withdraw
                         4.Enter 4 to check balance
                         5.Enter 5 to exit
""")
        if user_input=='1':
            self.create_pin()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='2':
            self.deposite()
        elif user_input=='4':
            self.check_balance()
        else :
            print("Bye,Thank you for using Atm")
    
    def create_pin(self):
        self.__pin=input("Enter your Pin:")
        print("Pin set successfully")

    def deposite(self):
        temp=input("Enter your pin:")
        if temp==self.__pin:
            amount=int(input("Enter the amount"))
            self.__balance=self.__balance+amount
            print("Deposite Successful")
        else:
            print("invalid pin")

    def withdraw(self):
        amount=int(input("Enter the amount:"))
        temp=input("Enter your pin:")
        if temp==self.__pin:
            if amount<self.__balance:
                self.__balance=self.__balance-amount
                print("Operation Successful")
            else:
                print("insufficient Balance")
        else:
            print("invalid pin")

    def check_balance(self):
        temp=input("Enter your pin:")
        if temp==self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")


        
Sbi=Atm()

while 1:
    option=int(input("Enter the menu number:"))
    if option in [1,2,3,4]:
        Sbi.menu()
    else:
        Sbi.menu()
        break
