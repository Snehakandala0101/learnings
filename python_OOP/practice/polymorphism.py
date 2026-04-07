
#Method overriding(Run time polymorphism)
class Animal:
    def sound(self):
        print("animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals=[Dog(), Cat() ,Animal()]
for a in animals:
    a.sound()  # same method sound() behaves differently depending on the object(dog,cat,animal)



#function/operator polymorphism
def add(a,b):
    return a+b

print(add(5,10))
print(add("Hi ", "Ana"))


#polymorphism with inheritance

class Employee:
    def work(self):
        print("employee is working")
class Developer(Employee):
    def work(self):
        print("Developer is coding")
class Manager(Employee):
    def work(self):
        print("Manager is managing")

#using polymorphism
def perform_work(emp):    #this function does't care if it's a developer or manager Object
    emp.work()

dev=Developer()
mgr=Manager()
emp=Employee()

perform_work(emp)
perform_work(dev)
perform_work(mgr)