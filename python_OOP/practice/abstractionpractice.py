# abstraction using abstract method
from abc import ABC, abstractmethod

#abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

#child class
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side * self.side

#child class2        
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
        

s=Square(6)
print(s.area())
c=Circle(2)
print(c.area())




#using concrete method
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass  # Abstract: child must define

    # Concrete method
    def start(self):
        print("Vehicle started")

# Child class: Car
class Car(Vehicle):
    def fuel_type(self):
        return "Petrol"

# Child class: ElectricBike
class ElectricBike(Vehicle):
    def fuel_type(self):
        return "Electricity"

# Testing
v1 = Car()
v2 = ElectricBike()

# Using concrete method from abstract class
v1.start()  # Vehicle started
v2.start()  # Vehicle started

# Using abstract method implemented by child
print(v1.fuel_type())  # Petrol
print(v2.fuel_type())  # Electricity
            
