# Inheritance in Python

- **Inheritance allows a class (child class) to acquire properties and methods of another class (parent class).**
- It promotes code reusability and establishes a relationship between classes.

---
## Real-Life Example

Think of:
- Parent: Animal
- Child: Dog
Dog automatically has:
- eat()
- sleep()
But Dog can also have:
- bark()
Dog reuses parent features and adds new features.

---
## Basic Syntax
```python
class Parent:
    pass

class Child(Parent):
    pass
```

Child class inherits from Parent class.

**Simple Example**
```python
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()
d.bark()
```
**Output**
```
Animal eats
Dog barks
```

Dog can access both:
- Parent method → eat()
- Child method → bark()
--- 
## super() Function

super() is used to call parent class constructor or methods.

**Example with Constructor**
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Buddy", "Golden Retriever")
print(d.name)
print(d.breed)
```
**Why super()?**

Without ```super()```, parent variables won’t initialize.

---
## Types of Inheritance
#### 1️⃣ Single Inheritance

One parent → One child
```
    Animal
       ↑
      Dog
```
```python
class Animal:
    pass

class Dog(Animal):
    pass
```

#### 2️⃣ Multilevel Inheritance

Parent → Child → Grandchild
```
    Animal
       ↑
      Dog
       ↑
     Puppy
```
```python
class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass
```

#### 3️⃣ Multiple Inheritance

Child inherits from multiple parents.
```
   Father     Mother
      \          /
       \        /
         Child
```
```python
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def talent(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()
c.talent()
```
#### 4️⃣ Hierarchical Inheritance

One parent → Multiple children
```
        Animal
       /      \
     Dog      Cat
```
```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass
```
#### 5️⃣ Hybrid Inheritance

Combination of multiple types.
```
        A
       / \
      B   C
       \ /
        D
```
Python supports this.

---
## How Inheritance Works Internally

Flow:
```
Object Created
      ↓
Search in Child Class
      ↓
If not found → Search in Parent Class
      ↓
Execute method
```


#### Advantages of Inheritance

:white_check_mark: Code reuse
:white_check_mark: Reduces duplication
:white_check_mark: Improves readability
:white_check_mark: Better organization
:white_check_mark: Easy extension of features

#### Disadvantages

:x: Tight coupling between classes
:x: Can make debugging harder
:x: Deep inheritance reduces clarity
:x: Improper design causes confusion


