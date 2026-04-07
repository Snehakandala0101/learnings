# Class ,Objects, Instance, and Constructor in Python
---
## 1. Class:
-  A **Class** is a blueprint or template for creating objects. 
- It defines attributes(variables) and methods( functions) that the objects are created from the class will have.

**Syntax**
```python
class ClassName:
    #attributes
    #methods
```
**Example:**

```python
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print(f"Car: {self.brand}{self.model})
```
**Explanation:**
- Car is a class.
-  ```__init__``` is a constructor.
- self represents the instance of the class.

### Advantages
1. Code Reusability
2. Better Organization
3. Easy maintenance
4. Real-world modeling

---

## 2.Objects:
An **Object**  is an instance of a class. It is a real_world entity created from the class blueprint.

**Creating Objects:**
```python
my_car= Car("Toyota","Corolla")
my_car.display_info()
```
**Explanation:**
- my_car is an object of the class Car.
- Objects store data(attributes) and can perform actions (methods).

---
## 3.Instance Variables:
Instance variables are attributes **unique to each object**. They  are defined using self.

**Example:**
```python
class Student:
    def __init__(self,name,age):
        self.name=name     #instance variable
        self.age=age       #instance variable
s1=Student("Sana", 16)
s2=Student("Sonu",14)
print(s1.name,s1.age)
print(s2.name,s2.age)
```
**Explanation:**
- s1 and s2 are **different instances**, each with its own data.

---
## 4.Constructors:
A **constructor** is a special method that 
- automatically runs when an object is created.
- used to initialize object variables
In Python, the constructor method is always ```__init__()```.

**Syntax:**
```python
class ClassName:
    def __init__(self,parameters):
        #initialize object
```
**Example:**
```python
class Person:
    def __init__(self,name,age):
        self.name=name     
        self.age=age       
p1=Person("Sana", 16)
print(p1.name,p1.age)
```
**Key Points:**
- ```__init__``` initializes the object with values.
- Can have **parameters** to pass values during object  creation.
- Multiple objects can have different values using the constructor.

### Types of Constructors
|Type     |  Description   |
|:--------|:---------------:|
|Default Constructor | No Parameters  |
| Paarameterized Constructor  | Takes arguments  |

### Advantages
- Initializes object properly.
- Reduces repeetitive code.
- Ensures data consistency.

--- 
### Comparison Table
| Feature | Description | Example |
|:--------|:-----------:|:--------|
|Class    |Blueprint for objects |class Car:  |
|Object   |Instance of a class|my_car=Car() |
|Instance Variable|Attribute unique to each object |self.name=name |
|Constructor | Initializes object attributes automatically|```def __init__(self,name):```|