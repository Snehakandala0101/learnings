# 📘 Dictionaries in Python

## 🔹 Definition

A *Dictionary* is a built-in data structure in Python that stores data in *key-value pairs*.

- Defined using curly braces { }
- Keys must be unique
- Mutable (can modify, add, remove)
- Ordered (Python 3.7+ maintains insertion order)

python
student = {
    "name": "Sneha",
    "marks": 95,
    "course": "EEE"
}


---

# 🔹 Key Properties of Dictionaries

| Property | Description |
|------------|------------|
| Key-Value Pair | Data stored as key : value |
| Mutable | Can modify values |
| Unique Keys | Duplicate keys not allowed |
| Ordered | Maintains insertion order |
| Fast Lookup | O(1) average time complexity |

---

# 🔹 Creating Dictionaries

python
# Empty dictionary
d = {}

# Using dict() constructor
student = dict(name="Sneha", marks=95)

# Dictionary with different data types
data = {
    "id": 101,
    "name": "Python",
    "price": 299.99,
    "available": True
}


---

# 🔹 Accessing Values

python
student = {"name": "Sneha", "marks": 95}

student["name"]        # Direct access
student.get("marks")   # Safe access


⚠️ get() does not raise error if key not found.

python
student.get("grade", "Not Available")


---

# 🔹 Adding & Updating Elements

python
student = {"name": "Sneha", "marks": 95}

# Add new key
student["grade"] = "A"

# Update value
student["marks"] = 98

# Using update()
student.update({"course": "EEE"})


---

# 🔹 Removing Elements

python
student = {"name": "Sneha", "marks": 95, "course": "EEE"}

student.pop("marks")     # Remove specific key
del student["course"]    # Delete key
student.clear()          # Remove all elements


---

# 🔹 Dictionary Methods

| Method | Purpose |
|----------|---------|
| get() | Access value safely |
| keys() | Returns all keys |
| values() | Returns all values |
| items() | Returns key-value pairs |
| pop() | Removes key |
| update() | Updates dictionary |
| clear() | Removes all elements |

Example:

python
student = {"name": "Sneha", "marks": 95}

print(student.keys())
print(student.values())
print(student.items())


---

# 🔹 Looping Through Dictionary

### ➤ Loop through keys

python
for key in student:
    print(key)


### ➤ Loop through values

python
for value in student.values():
    print(value)


### ➤ Loop through key-value pairs

python
for key, value in student.items():
    print(key, value)


---

# 🔹 Nested Dictionary

python
students = {
    "s1": {"name": "Sneha", "marks": 95},
    "s2": {"name": "Rahul", "marks": 90}
}

print(students["s1"]["name"])


---

# 🔹 Dictionary Comprehension

python
nums = [1, 2, 3, 4]

square_dict = {x: x*x for x in nums}
print(square_dict)


With condition:

python
even_squares = {x: x*x for x in range(10) if x % 2 == 0}


---

# 🔹 Built-in Functions

python
len(student)
max(student)   # Works on keys
min(student)


---

# 🔹 Time Complexity

| Operation | Time Complexity |
|------------|-----------------|
| Access | O(1) |
| Insert | O(1) |
| Delete | O(1) |
| Search | O(1) |

(Implemented using hash tables)

---

# 🔹 Important Rules

- Keys must be immutable (int, str, tuple).
- Lists cannot be dictionary keys.
- Values can be any data type.
- Duplicate keys are not allowed.

Example:

python
d = {
    1: "one",
    (2, 3): "tuple key"
}


---

# 🔹 Dictionary vs List

| Feature | Dictionary | List |
|-----------|-------------|------|
| Structure | Key-Value | Indexed |
| Access | By key | By index |
| Speed | Faster lookup | Slower search |
| Duplicate Keys | Not allowed | Allowed |

---

# 🔹 When to Use Dictionary?

✅ Fast lookup by key  
✅ Storing structured data  
✅ Mapping relationships  
✅ Counting frequency of elements  

---

# 🔹 Important Points

- Dictionaries use hashing internally.
- Python 3.7+ maintains insertion order.
- get() is safer than direct indexing.
- Average time complexity is O(1).

---

# 🎯 Summary

Use *Dictionaries* when:
- You need key-value mapping
- You want fast access
- You need structured data storage
