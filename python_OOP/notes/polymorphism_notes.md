# Polymorphism in Python 
---
Polymorphism is a core concept of Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common superclass.
+ The term **polymorphism** literally means **many forms**.
+ The same method name, operator, or function can behave differently for different types of objects.
+ Polymorphism increases flexibility, reusability, and maintainability of code.
---
### Purpose of Polymorphism
- **Flexibility:** Use the same method or interface for different object types.
- **Code Reusability:** Write generic code that works with multiple classes.
- **Simplifies Maintenance:** Reduces code duplication; adding new classes doesn’t break existing code.
- **Supports OOP Principles:** Works with inheritance, abstraction, and interfaces.
---
### Types of Polymorphism in Python
1. **Compile-Time Polymorphism (Method Overloading)**
- Achieved when same method name behaves differently based on different parameters.
- Python does not support traditional method overloading, but  we can simulate it using:
    - Default arguments
    - Variable-length arguments (*args, **kwargs)

**Example:**
```python
class Calculator:

    # Method with default argument
    def add(self, a, b=0):
        return a + b

calc = Calculator()
print(calc.add(5))      # Output: 5
print(calc.add(5, 10))  # Output: 15
```
**Notes:**
Method signature can be flexible using default or variable-length arguments.

2. **Run-Time Polymorphism (Method Overriding)**
* Achieved via inheritance.
* Subclass redefines a method of the parent class.
* The method to call is determined at runtime, depending on the object type.

**Example:**
```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Using polymorphism
def animal_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Dog barks
animal_sound(cat)  # Output: Cat meows
```
**Key Points:**
:bulb: The same method name speak() works differently for different objects.
:bulb: Supports dynamic behavior, enhancing code flexibility.

3. **Operator Overloading**
- The same operator behaves differently depending on the operand types.
- Achieved in Python using special methods (dunder methods like ```__add__```,``` __mul__```).

**Example:**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"({self.x}, {self.y})")

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
p3.display()  # Output: (6, 8)
```
4. **Duck Typing Polymorphism**
- Python is dynamically typed; an object’s type is determined at runtime.
- Any object that implements the required methods can be used, regardless of class.

**Example:**
```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

# Duck typing
def lets_fly(flyable):
    flyable.fly()

bird = Bird()
plane = Airplane()

lets_fly(bird)   # Bird is flying
lets_fly(plane)  # Airplane is flying
```
:bulb: **Note:** “If it walks like a duck and quacks like a duck, it’s a duck.” – Python does not require inheritance for polymorphism.

---

### Key Points of Polymorphism
-  Polymorphism allows one interface, multiple implementations.
-  Works naturally with:
    -  Inheritance → method overriding
    -  Abstract classes → subclasses implement abstract methods
    -  Operators → operator overloading
    -  Duck typing → dynamic typing flexibility
- Enhances code flexibility, readability, and maintainability.
---
#### Advantages of Polymorphism
|Advantage	|Description|
|:-----------|:---------|
Code Reusability	|Same interface can work with different object types.|
Flexibility	|Add new classes with minimal code changes.|
Simplifies |Maintenance,Reduces duplication and increases modularity.|
Supports |OOP Principles	Works with inheritance and abstraction.|
Enhances Readability|	Same method/operator works consistently across objects.|

---
##### Real-World Examples
- Payment Systems:
pay(amount) → works differently for CreditCard, DebitCard, UPI, PayPal.
- Shapes:
area() → different calculation for Circle, Square, Triangle.
- Vehicles:
start_engine() → behaves differently for Car, Bike, Truck.
- Animal Sounds:
speak() → different animals produce different sounds.

---
#### Polymorphism vs Abstraction vs Encapsulation
|Feature|	Polymorphism	|Abstraction	|Encapsulation|
|:------|:-------------|:-----------|:-------|
|Definition|	One interface, multiple forms|	Hides implementation details|	Hides data (private/protected)|
|Purpose|	Flexibility, reusability|	Reduce complexity	|Protect data integrity|
|Implementation	|Method overriding, operator overloading|	Abstract classes, methods|	Access modifiers, getters/setters
When Decided|	Runtime / Compile-time|	Design time	|Design time|