class Bank_Acc:
    def __init__(self,name,acc_number, balance):
        self.name = name
        self.acc_number = acc_number
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self):
        try:
            amount = int(input("Enter the amount: "))
        except ValueError:
            print("Please enter a numeric value")
            return 
    
        if  amount <= 0:
            print("Please enter a vaild amount!")
        else:
            self.__balance += amount    
            print(f"Amount has been succssfully credited to you acc. New balance is {self.get_balance()}$")
    
    def withdraw(self):
        try:
            amount = int(input("Enter the amount: "))
        except ValueError:
            print("Please enter a numeric value")
            return 
        if  amount <= 0:
            print("Please enter a vaild amount!")
        while amount > self.__balance:
            print("You dont have sufficient balance!")
            try:
                amount = int(input("Enter the amount: "))
            except ValueError:
                print("Please enter a numeric value")
                return 
            if  amount <= 0:
                print("Please enter a vaild amount!")
  
        self.__balance -= amount    
        print(f"Your account has been debited with {amount}$. New balance is {self.get_balance()}$")
  
            

    def display_info(self):
        print(f"Name : {self.name}" )
        print(f"Account Number: {self.acc_number}")
        print(f"Balance amount: {self.get_balance()}$")






Account1 = Bank_Acc("Tom", "112234", 2000)

#Account1.display_info()

Account1.withdraw()