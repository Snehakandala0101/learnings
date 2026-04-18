# 🧠 Python First-Class Functions, Closures & Decorators 

## :one: First-Class Functions

📌 What Does **First-Class** Mean?

When we say Python treats functions as first-class citizens, it means:

> A function is treated like any other variable or object.

Just like:
- Integers
- Strings
- Lists

Functions can also:

- Be assigned to variables
- Be passed as arguments
- Be returned from other functions
- Be stored in data structures
---
### Why Does This Matter?

Because this ability allows:
* Functional programming
* Closures
* Decorators
* Callbacks
* Higher-order functions

> Without first-class functions → decorators wouldn’t exist.

##### :bulb: Note

In Python:
- A function is an object in memory.
- When you define a function:
    - Python creates a function object
    - That object has:
        - Name
        - Memory address
        - Code block
        - Metadata

- The function name is simply a reference pointing to that object.
- So if you assign:
    - Another variable to that function
    - Now two variables point to the same function object.

**Example:**
```python
def greet():
    return "Hello"

say_hello = greet
print(say_hello())
```

- greet is a function object.
- `say_hello = greet` does NOT call the function.
- It simply makes say_hello point to the same function object.
- Now both names refer to the same function in memory.
- So when we call `say_hello()`
- it behaves exactly like `greet()`.

This Proves First-Class Behavior.Because:
* We assigned a function to a variable.
* Just like assigning a number: `x = 10`
* Functions are treated like normal values.
---
### Higher-Order Functions

A Higher-Order Function is a function that:
- Takes another function as input
OR
- Returns another function
> This is possible only because functions are first-class.

### Higher-Order Functions are Powerful

They allow:
- Code reusability
- Flexible behavior
- Cleaner abstraction
- Functional programming patterns

> Decorators are higher-order functions.
---
## :two: Closures
A closure happens when:
- A function is defined inside another function
- The inner function uses variables from the outer function
- The outer function finishes execution
- But the inner function still remembers those variables

**Key Concept**
Normally:
- Local variables are destroyed after a function finishes.
- But in closures:
    - Python preserves those variables
    - Because the inner function still needs them

This preserved environment is called: **A Closure**

---
#### What Does a Closure Store?

A closure stores:
1. The function code
2. The free variables (variables from outer scope)
3. A reference to the enclosing environment
This is stored in something called a cell object internally.

---
#### Why Closures Exist

Closures allow:
+ Data hiding
+ Function factories
+ Persistent state without using global variables
+  Creation of decorators

---
##### NOTE
Each time you call the outer function:
- A new memory environment is created
- Each returned inner function gets its own preserved variables
- They do NOT share memory unless explicitly designed to.
---
##### Example:
```python
def outer():
    message = "Hello"
    
    def inner():
        print(message)
        
    return inner

func = outer()
func()
```
1. outer() runs.
2. message = "Hello" is created.
3. inner() is defined inside outer().
4. outer() returns inner.
5. Normally, local variables should disappear.
6. But inner() still remembers message.
7. When we call func(), it prints:
```python
Hello
```
Even though outer() has already finished.

---
## Scope and LEGB Rule

To fully understand closures and decorators, you must understand scope resolution.

Python follows the LEGB Rule:

L → Local
E → Enclosing
G → Global
B → Built-in

When Python looks for a variable:
- It checks Local
- Then Enclosing
- Then Global
- Then Built-in

> Closures work because of the Enclosing scope.
---
### The `nonlocal` Keyword

Inside closures:

If you want to modify a variable from the enclosing scope,
you must use: `nonlocal`
- Because without it:
Python assumes you're creating a new local variable.
- nonlocal tells Python:
> Use the variable from the enclosing function.

---
## :three: Decorators

A decorator is:
- A function that takes another function,
- adds extra functionality,
- and returns a new function.

All this:
> Without modifying the original function’s source code.

**Core Idea**

Decorators are built using:
- First-class functions
- Closures
- Higher-order functions

So decorators are NOT magic.
They are simply structured closures.

---
### How Decorators Work Internally

When Python sees:
```python
@decorator
def my_function():
```
Python internally converts it to:
```
my_function = decorator(my_function)
```
So:
- The original function is passed into the decorator
- The decorator returns a wrapper function
- That wrapper replaces the original function reference
- Now when you call `my_function()`,you’re actually calling the wrapper.
---
### What is a Wrapper Function?

Inside decorators, we usually create:
`A wrapper function`
This wrapper:
1. Executes additional logic
2. Calls the original function
3. Returns the result

The wrapper has access to:
- The original function
- Its arguments
- The enclosing environment (closure)
---
### Why Use *args and **kwargs?

> Because decorators should work for ANY function.
> If you hardcode parameters,your decorator becomes limited.

Using:
- `*args` → captures positional arguments
- `**kwargs` → captures keyword arguments

This makes your decorator flexible.

---
### Why Use functools.wraps()?

When we wrap a function:

The original function’s:
- Name
- Docstring
- Metadata

Are replaced by the wrapper’s.

To preserve metadata, we use:

`functools.wraps()`

It copies metadata from the original function to the wrapper.

This is important for:

- Debugging
- Documentation
- Frameworks like Flask/Django
---
#### Decorator With Arguments (Advanced)

Sometimes decorators themselves need parameters.

In that case:

We need three layers:
1. Outer function → takes decorator arguments
2. Decorator function → takes original function
3. Wrapper function → executes logic

This works because:
- Functions can return functions
- Closures preserve values
- Python supports nested scopes
---
##### Example:
```python
def my_decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()
```
When Python sees:
```
@my_decorator
def greet():
```
It internally does:
```
greet = my_decorator(greet)
```
So now:

greet is replaced by wrapper
When we call `greet()`, it actually calls `wrapper()`
**Output:**
```
Before execution
Hello
After execution
```
---
##### Real-World Uses of Decorators

Decorators are widely used in:
- Logging systems
- Authentication systems
- Access control
- Caching
- Measuring execution time
- Rate limiting
- Input validation
- Web frameworks
- APIs

Decorators help keep code:
+ Clean
+ Modular
+ Reusable
---
##### Model to Remember
- First-class functions → allow functions as values
- Closures → allow memory retention
- Decorators → use both to enhance behavior

So the chain is:
```
Functions as objects
        ↓
Higher-order functions
        ↓
Closures
        ↓
Decorators
```
---
##### Common Mistakes
* Forgetting return wrapper
* Forgetting to return original function result
* Not using *args, **kwargs
* Forgetting nonlocal
* Not preserving metadata
* Confusing decorator arguments with function arguments

---
##### Summary

A decorator is a higher-order function that takes another function as input, adds additional functionality using closures, and returns a modified function without altering the original function’s source code.