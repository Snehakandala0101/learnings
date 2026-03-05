# 📌 Python Functions, Scope, *args, **kwargs – Complete Notes

This README summarizes Python functions, variable scope, and flexible arguments for practice.  

---

## 1️⃣ Functions in Python

**Definition:**  
A function is a reusable block of code that performs a specific task.

**Syntax:**

```python
def function_name(parameters):
    """Optional docstring"""
    # code
    return result  # optional
```
**Example:**
```python
def greet(name):
    print("Hello", name)
greet("Sneha")  # Output: Hello Sneha
```
### Key Points:

- Functions improve code reusability and modularity.
- return is optional; if not used, function returns None.
- Functions can accept positional arguments, keyword arguments,   *args, and **kwargs.
- Always give meaningful names to functions and parameters.

---
## 2️⃣ Scope in Python
**Definition**:
Scope determines where a variable can be accessed in the code.

#### Local Variable Syntax:
```python
def my_func():
    local_var = 10  # Accessible only inside this function
```

#### Global Variable Syntax:
```python
global_var = 0  # Accessible everywhere
```

**Example:**
```python
# Global variable
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
```
### Key Points:
- Local variables exist only inside the function.
- Global variables exist throughout the program.
- To modify a global variable inside a function, use global.
- Avoid overusing global variables; prefer returning values from functions.

---
## 3️⃣ *args (Arbitrary Positional Arguments)

**Definition**:
*args allows a function to accept any number of positional arguments.

**Syntax**:
```python
def function_name(*args):
    # args is a tuple
    pass # accepts multiple inputs
```
**Example:**
```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)

sum_numbers(1, 2, 3)  # Output: 6
```

### Key Points:
- *args stores all extra positional arguments as a tuple.
- Useful when the number of inputs is unknown or variable.
- Can be combined with normal positional arguments and **kwargs.
---

## 4️⃣ **kwargs (Arbitrary Keyword Arguments)

**Definition:**
**kwargs allows a function to accept any number of keyword arguments.

**Syntax:**
```python
def function_name(**kwargs):
    # kwargs is a dictionary
    pass
```
**Example:**
```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display_info(name="Sneha", age=22)
# Output:
# name : Sneha
# age : 22
```

### Key Points:
- **kwargs stores arguments as a dictionary.
- Useful for flexible, named parameters.
- Can be combined with normal arguments and *args.
- Use .items() or .values() to access the dictionary elements.
---

## 5️⃣ Combining *args and **kwargs

**Definition:**
A function can accept normal arguments, *args, and **kwargs together.
**Syntax:**
```python
def function_name(normal_arg, *args, **kwargs):
    pass
```
**Example:**
```python
def student_info(name, *marks, **details):
    print("Name:", name)
    print("Marks:", marks)
    print("Details:", details)

student_info("Sneha", 90, 85, age=22, city="Hyderabad")
# Output:
# Name: Sneha
# Marks: (90, 85)
# Details: {'age': 22, 'city': 'Hyderabad'}
```
### Key Points:
- Order matters: **normal arguments → *args → kwargs
- Enables flexible, reusable functions that handle variable inputs.
- Useful for functions like student info, logging utilities, or general-purpose handlers.
---
## 6️⃣ Global vs Local Variables

**Definition:**

**Local:** Exists only inside a function.

**Global:** Exists throughout the program.

**Syntax to modify global variable:**
```python
global_var = 0

def modify():
    global global_var
    # modify global_var
```

### Key Points:
- Use global to modify global variables inside a function.
- Local variables cannot be accessed outside their function.
- Best practice: prefer returning values instead of using global variables.
---
## ✅ Summary / Best Practices
- Functions allow reusable, modular code.
- Use small, focused functions — one function = one task.
- *args → variable positional inputs stored as tuple.
- **kwargs → variable keyword inputs stored as dictionary.
- Combine *args and **kwargs for flexible function design.
- Minimize global variable usage, prefer returning values.
- Always handle edge cases in your functions.
- Use meaningful names and docstrings for clarity.