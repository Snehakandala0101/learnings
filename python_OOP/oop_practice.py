#creating a student class
class Student:
    name="Sneha"
    age=22
s1=Student()
print(s1.name,s1.age)

#initializing using constructor
class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
c1=Car("Toyota",1500000)
print(c1.brand,c1.price)


#method inside a class
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name: ",self.name,"Salary: ",self.salary)

E1=Employee("Rahul",50000)
E1.display()

#calculate area using a class
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calc_area(self):
        print("area= ",self.length*self.breadth)
r1=Rectangle(10,20)
r1.calc_area()

#class variable example
class Student:
    college="ABC College"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age,self.college)
s1=Student("Sneha",22)
s1.display()

#count number of objects
class Person:
    count=0
    def __init__(self,name):
        self.name=name
        Person.count+=1
p1=Person("Inshaan")
p2=Person("Anan")
p3=Person("Amog")
print("Total Persons:",Person.count)

#Bank Account example
class BankAccount:
    def __init__(self,name,balance,deposit_amount,with_draw):
        self.name=name
        self.balance=balance
        self.deposit_amount=deposit_amount
        self.with_draw=with_draw
    def deposit(self):
        print("deposit amount=",self.deposit_amount)
        print("final balance:",self.deposit_amount+self.balance)
    def withdraw(self):
        print("withdraw amount=",self.with_draw)
        print("Total balance=",self.balance-self.with_draw)
b1=BankAccount("Harsha",2000,5000,0)
b2=BankAccount("Vansh",40000,0,15000)
b1.deposit()
b2.withdraw()

#student grade system
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_grade(self):
        if self.marks>90:
            print("Grade A")
        elif self.marks<90 and self.marks>75:
            print("Grade B")
        elif self.marks<75 and self.marks>50:
            print("Grade C")
        else:
            print("Fail")
s1=Student("rohit",40)
s2=Student("Mohit",88)
s1.display_grade()
s2.display_grade()


#creating multiple objects and printing them
class Laptop:
    def __init__(self,brand,RAM):
        self.brand=brand
        self.RAM=RAM
    def details(self):
        print(self.brand,self.RAM)
l1=Laptop("HP","16GB")
l2=Laptop("Dell","8GB")
l3=Laptop("Lenovo","16GB")
Laptop.details(l1)
Laptop.details(l2)
Laptop.details(l3)
        



