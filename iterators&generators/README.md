# ITERATORS AND GENERATORS IN PYTHON
---

## Iterators in Python

#### Iterable
An iterable is any object that can be looped over.
**Examples:**
- list
- tuple
- string
- set
- dictionary

An iterable:
+ Has ```__iter__()``` method
+ Can be used inside a ```for``` loop
**Example:**
```python
numbers = [1, 2, 3]
```
---
### ITERATOR
An iterator is an object that:

- Remembers its position during iteration
- Returns one element at a time
- Stops when no elements are left
In simple words:
** An iterator gives values one by one instead of all at once.**
An iterator:
- Has both ```__iter__()``` and ```__next__()``` methods
---
### How Iteration Works Internally

When you write:
```python
for x in numbers:
    print(x)
```
Python internally does this:
- Converts numbers into an iterator using ```iter()```
- Gets the next value using ```next()```
- Repeats until StopIteration error occurs

---
### Iterator Functions
:diamonds: ```iter()```

Converts an iterable into an iterator
```python
nums = [1, 2, 3]
it = iter(nums)
```
:diamonds: ```next()```

Returns the next element
```python
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
```
After elements finish:
```python
 next(it)  # StopIteration error
```
---
### Iterable vs Iterator
Iterable|	Iterator|
|:----|:----|
Can be looped over|	Produces next value|
Example: list, tuple, string|	Created using iter()
Has ```__iter__()```	|Has ```__next__()```

---
### Creating a Custom Iterator

To create your own iterator class, you must define:
- ```__iter__()```
- ```__next__()```

Example concept:
```python
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
```
---

## GENERATORS

A **generator** is a simpler way to create iterators using the yield keyword.
- Instead of returning all values at once, it yields one value at a time.

:diamonds: **Generator Function**
```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
```
Using it:
```python
for num in count_up_to(5):
    print(num)
```
Output:
```python
1
2
3
4
5
```
---
### Why Generators Are Powerful
:one: **Memory Efficient**
- They don’t store all values in memory.
- Useful for large data (files, big datasets, ML pipelines).

:two: **Faster Execution**
- Values are produced only when needed.

---
#### Generator vs Normal Function
**Normal function:**
```python
def nums():
    return [1, 2, 3]
```
Creates full list in memory.

**Generator:**
```python
def nums():
    yield 1
    yield 2
    yield 3
```
Produces values one by one.

Feature|	Normal Function|	Generator|
|:-----|:-----|:-----|
Keyword Used	|`return`|	`yield`|
How Values Are Produced|	Returns all values at once	|Produces one value at a time
Execution|	Executes completely and stops|	Pauses at yield and resumes later|
Memory Usage|	Stores entire result in memory|	Generates values lazily (memory efficient)|
Return Type|	Returns actual value (int, list, string, etc.)|	Returns a generator object|
Reusability|	Returned data can be reused|	Once exhausted, must recreate generator|
Suitable For|	Small or fixed-size data	|Large datasets / streaming data|
Performance|	May consume more memory	|More efficient for large data|
Control|	No pause-resume mechanism	|Has pause-resume capability|

---
#### Generator Expression (Like List Comprehension)

**List comprehension:**
```python
squares = [x*x for x in range(5)]
```
**Generator expression:**
```python
squares = (x*x for x in range(5))
```
**Notice () instead of []**

---
#### Iterator vs Generator 
Feature|	Iterator	|Generator|
|:-----|:-----:|:-----:|
Creation	|Using class|	Using yield|
Code complexity|	More	|Very simple|
Memory efficient|	Yes|	Yes|
Readability|	Less	|More|

---
##### When Should You Use What?

:heavy_check_mark: Use generators when:

- Working with large files
- Processing streaming data
- Building pipelines
- ML data preprocessing

:heavy_check_mark: Use custom iterators when:

- You need full control over iteration logic
- You want structured class-based design

---
###### Key Takeaways
* Iterable → Can be looped over
* Iterator → Produces next value
* for loop internally uses ```iter()``` and ```next()```
* Generators simplify iterator creation
* Generators are memory efficient due to lazy evaluation