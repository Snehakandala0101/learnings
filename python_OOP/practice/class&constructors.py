#creating a class,initializing attributes ,creating two objects and printing their details

class Car:    #defining the car class
    def __init__(self,brand,model):  #constructor
        self.brand=brand
        self.model=model

#creating objects
c1=Car("Tata","Nexon")
c2=Car("Hyundai","Creta")

#print details
print(f"CAR1: Brand= {c1.brand}, Model={c1.model}")
print(f"CAR2: Brand= {c2.brand}, Model={c2.model}")


#another example

class Laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    
    def discount(self,price_reduction):
        self.price-=price_reduction
        print(f"Discount Applied!! New price: {self.price}")

l1=Laptop("Dell","Inspiron 15",60000)
print(f"original Price: {l1.price}")
l1.discount(5000)

#example
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello, my name is {self.name} and Iam {self.age} year old")
student1=Student("Alyzha",15)
student2=Student("Radhi",14)
student1.greet()
student2.greet()

