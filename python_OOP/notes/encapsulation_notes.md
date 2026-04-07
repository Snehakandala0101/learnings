# Encapsulation
---
Encapsulation means Wrapping data (variables) and methods together inside a class and restricting direct access.
It helps in:
- Data hiding
- Protecting sensitive data
- Controlling access to variables

---
## Why Encapsulation is Needed?

Without encapsulation:
- Anyone can modify variables directly.
- Data may become inconsistent.
- Security issues may occur.
- Debugging becomes difficult.

Encapsulation ensures:
- Controlled access
- Validation before modification
-  Secure code structure

---
## Real-Life Example

Think of an ATM machine:

- You cannot directly access bank balance.
- You must enter PIN.
- You use methods like:
    - deposit()
    - withdraw()
    - check_balance()

You don’t see how it works internally.
That is **Encapsulation**.

---
## Access Modifiers in Python

Python does not have strict access modifiers like Java, but it follows naming conventions.

|Type	|Syntax |	Meaning |
|:------|:------:|:----------|
|Public|	```variable```|	Accessible anywhere|
|Protected|	```_variable```|	Should not be accessed outside class (convention)|
|Private|	```__variable```|	Strongly restricted (name mangling applied)|

---
## Types of Encapsulation in Python
##### 1. Public Members

Accessible from anywhere.
```python
class Student:
    def __init__(self):
        self.name = "Sneha"   # Public variable

s = Student()
print(s.name)   # Accessible
```
##### 2. Protected Members

Single underscore``` _variable```
```python
class Student:
    def __init__(self):
        self._marks = 90   # Protected

s = Student()
print(s._marks)  # Possible but not recommended
```

- Used mainly in inheritance.

##### 3. Private Members

Double underscore ```__variable```
```python
class Bank:
    def __init__(self):
        self.__balance = 1000   # Private variable

b = Bank()
print(b.__balance)   # Error
```
---

## What is Name Mangling?

When we use ```__variable```, Python internally changes its name.

Example:
```python
print(b._Bank__balance)
```

Python internally converts:

```__balance → _Bank__balance```

This prevents accidental access.

---
## Getters and Setters

To access private variables safely, we use methods.

**Example**
```python
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid amount")

b = Bank(1000)

print(b.get_balance())   # Access via getter
b.set_balance(2000)      # Modify via setter
print(b.get_balance())
```

---
## Encapsulation with Validation

Encapsulation allows adding logic before updating data.

**Example:**
```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def set_salary(self, amount):
        if amount >= 10000:
            self.__salary = amount
        else:
            print("Salary too low")

    def get_salary(self):
        return self.__salary
```

Here:
- Salary cannot be set below 10000.
- Data remains valid.
---
## Advantages of Encapsulation
&check; Data security
&check; Controlled modification
&check; Improves maintainability
&check; Prevents accidental changes
&check; Allows validation logic
&check; Makes debugging easier

---

## Disadvantages

- Slightly more code (getters/setters)
- Overuse can make code complex

---

## Encapsulation vs Abstraction
|Encapsulation	|Abstraction|
|:--------------|:----------|
|Hides data	|Hides implementation|
|Achieved using access modifiers|	Achieved using abstract classes|
|Focuses on data security|	Focuses on functionality|
|Example: Private variable|	Example: Abstract method|
