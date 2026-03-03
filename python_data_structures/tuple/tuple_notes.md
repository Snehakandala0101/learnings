# 📘 Tuples in Python

## 🔹 Definition

A *Tuple* is an ordered, immutable collection of elements in Python.

- Defined using parentheses ( )
- Allows duplicate values
- Supports indexing
- Cannot be modified after creation (immutable)

python
t = (1, 2, 3, 4)


---

# 🔹 Key Properties of Tuples

| Property | Description |
|-----------|------------|
| Ordered | Maintains insertion order |
| Immutable | Cannot add, remove, or modify elements |
| Duplicates | Allowed |
| Indexed | Supports positive & negative indexing |
| Faster | Slightly faster than lists |

Example:

python
numbers = (1, 2, 2, 3)
print(numbers)
# Output: (1, 2, 2, 3)


---

# 🔹 Creating Tuples

python
# Normal tuple
t1 = (10, 20, 30)

# Without parentheses
t2 = 1, 2, 3

# Single element tuple (Important!)
single = (5,)   # Comma is mandatory

# Empty tuple
empty = ()


---

# 🔹 Accessing Elements

python
nums = (10, 20, 30, 40)

nums[0]      # 10
nums[-1]     # 40
nums[1:3]    # (20, 30)


---

# 🔹 Tuple Unpacking

python
t = (10, 20, 30)

a, b, c = t
print(a, b, c)


Using * operator:

python
t = (1, 2, 3, 4, 5)

a, *b = t
print(a)  # 1
print(b)  # [2, 3, 4, 5]


---

# 🔹 Built-in Functions

python
t = (5, 2, 8, 1)

len(t)
max(t)
min(t)
sum(t)


---

# 🔹 Tuple Methods

Tuples have only two built-in methods:

python
t = (1, 2, 2, 3)

t.count(2)    # Count occurrences
t.index(3)    # Find index


---

# 🔹 Looping Through Tuple

python
t = (10, 20, 30)

for item in t:
    print(item)


Using index:

python
for i in range(len(t)):
    print(t[i])


---

# 🔹 Converting Tuple

### ➤ Tuple to List

python
t = (1, 2, 3)
l = list(t)


### ➤ List to Tuple

python
l = [1, 2, 3]
t = tuple(l)


---

# 🔹 Modifying Tuple (Indirect Way)

Since tuples are immutable, modification is done via conversion:

python
t = (1, 2, 3)

temp = list(t)
temp.append(4)
t = tuple(temp)

print(t)


---

# 🔹 Nested Tuple

python
nested = ((1, 2), (3, 4))

print(nested[0][1])  # Output: 2


---

# 🔹 Why Tuples Are Immutable?

- Provides data safety
- Prevents accidental modification
- Can be used as dictionary keys
- Improves performance

---

# 🔹 Tuple vs List

| Feature | Tuple | List |
|----------|--------|------|
| Syntax | () | [] |
| Mutable | ❌ No | ✅ Yes |
| Speed | Faster | Slower |
| Methods | Limited | Many |

---

# 🔹 Time Complexity

| Operation | Time Complexity |
|------------|-----------------|
| Access | O(1) |
| Search | O(n) |
| Count | O(n) |

---

# 🔹 When to Use Tuple?

✅ When data should not change  
✅ When you need fixed values  
✅ When using as dictionary keys  
✅ When performance matters  

---

# 🔹 Important Points

- Tuples are immutable.
- Stored in continuous memory.
- Faster than lists.
- Can contain mutable elements (like lists inside tuple).



---

# 🎯 Summary

Use *Tuples* when:
- You want fixed data
- You want better performance
- You need safe, unchangeable collections
