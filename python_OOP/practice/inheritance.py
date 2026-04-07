#single inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade=grade
    def show_grade(self):
        print(f"Grade={self.grade}")

stu1=Student("Mokshith",12,"A+")
stu1.display_info()
stu1.show_grade()


#Multilevel INheritance
class Vehicle:
    def start_engine(self):
        print("Engine started")
class Car(Vehicle):
    def drive(self):
        print("Driving")
class ElectricCar(Car):
    def charge(self):
        print("charging")

elec1=ElectricCar()
elec1.start_engine()
elec1.drive()
elec1.charge()

#Hierarchial inheritance
class Animal:
    def sound(self):
        print("animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

dog1=Dog()
dog1.sound()
cat1=Cat()
cat1.sound()

#constructor inheritance
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)   #super() to call the parent constructor
        self.department=department

emp1=Employee("Sonu",60000)     
print(emp1.name,emp1.salary)   
man1=Manager("Aliv",50000,"IT")
print(man1.name)
print(man1.department)
