# student marks class
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks  #private attribute
    
    #getter method 
    def get_marks(self):
        return self.__marks
    
    # setter method
    def set_marks(self,marks):
        if 0<= marks<=100:
            self.__marks=marks
            print(f"{self.name}'s marks updated to {self.__marks}")
        else:
            print("Invalid marks! Must be between 0 and 100")

    #method to display info
    def display_info(self):
        print(f"Student: {self.name},Marks={self.__marks}")

student1=Student("Vansh",85)
student1.display_info()

student1.set_marks(95)
student1.display_info()

student1.set_marks(120)
student1.display_info()
# trying to access private attribute directly
print(student1.__marks)  #attribute error


#another example 
class BankAccount:
    def __init__(self,initial_balance):
        self.__balance=initial_balance    #private attribute
        
    #deposit method
    def deposit(self,amount):
        if amount>=0:
            self.__balance+=amount
            print(f"deposited= {amount}")
        else:
            print("Deposit amount must be positive")
    #withdraw method
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"withdrawn={amount}")
        else:
            print("Insufficient balance")
    #getter method
    def get_balance(self): 
        return self.__balance
    # setter method
    def set_balance(self,amount):
        if amount>=0:
            self.__balance=amount
            print(f"balance is updated to: {self.__balance}")
        else:
            print("balance cannot be negative")

account=BankAccount(1000)
print(account.get_balance())

account.set_balance(1500)
print(account.get_balance())

account.set_balance(-500)
print(account.get_balance())
