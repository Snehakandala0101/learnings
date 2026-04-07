#encapsulation and polymorphism
class Employee:
    def __init__(self,name,salary):
        self.name=name       #public attribute
        self.__salary=salary  #private attribute(encapsulation)
    
    #getter method
    def get_salary(self):
        print(self.__salary)

    #setter method
    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("salary must be positive!")

    #work method(can be overriden)
    def work(self):
        print(f"{self.name} is working")
#subclass
class Manager(Employee):
    #override work method(polymorphism)
    def work(self):
        print(f"{self.name} is managing the team")

#create employee object
emp=Employee("Alice",50000)
print(emp.name)
emp.get_salary()
emp.work()

#update salary
emp.set_salary(55000)
emp.get_salary()

#try invalid salary
emp.set_salary(-1000)


#create manager object
mgr=Manager("Bob",80000)
print(mgr.name)
mgr.get_salary()
mgr.work()  #overriden work method

#update manager salar
mgr.set_salary(85000)
mgr.get_salary()

print("--------------------")


#abstraction,encapsulation,polymorphism
from abc import ABC, abstractmethod
class Device(ABC):
    def __init__(self,battery_level):
        self.__battery_level=battery_level #private attribute(encapsulation)
    #getter method
    def get_battery_level(self):
        return self.__battery_level
    #setter method
    def set_battery_level(self,level):
        if 0<=level<=100:
            self.__battery_level=level
        else:
            print("Battery level must be in 0 to 100")
    #abstract methods
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

#sub class1
class Laptop(Device):
    def turn_on(self):
        print(f"Laptop is turning on. Battery: {self.get_battery_level()}%.")
    def turn_off(self):
        print("Laptop is shutting down.")
#sub class2
class Smartphone(Device):
    def turn_on(self):
        print(f"Smartphone is turning on. Battery: {self.get_battery_level()}%.")
    def turn_off(self):
        print("SMartphone is turning off.")

#Laptop
laptop=Laptop(80)
laptop.turn_on()
laptop.set_battery_level(40)
print("Updated Laptop battery",laptop.get_battery_level())
laptop.turn_off()


#Smartphone
phone=Smartphone(50)
phone.turn_on()
phone.set_battery_level(40)
print("UPdated phone battery:",phone.get_battery_level())
phone.turn_off





