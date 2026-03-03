# 📘 Sets in Python

## 🔹 Definition

A *Set* is an unordered, mutable collection of unique elements in Python.

- Defined using curly braces { }
- Does NOT allow duplicate values
- Does NOT support indexing
- Uses hashing internally

python
s = {1, 2, 3, 4}


---

# 🔹 Key Properties of Sets

| Property | Description |
|-----------|------------|
| Unordered | No fixed position of elements |
| Mutable | Can add or remove elements |
| No Duplicates | Automatically removes duplicates |
| No Indexing | Cannot access elements by index |
| Fast Lookup | Membership checking is O(1) |

Example:

python
numbers = {1, 2, 2, 3}
print(numbers)
# Output: {1, 2, 3}


---

# 🔹 Creating Sets

python
# Normal set
a = {10, 20, 30}

# Empty set (Correct way)
b = set()


⚠️ {} creates an empty dictionary, not a set.

---

# 🔹 Adding Elements

python
s = {1, 2}

s.add(3)            # Add single element
s.update([4, 5])    # Add multiple elements


---

# 🔹 Removing Elements

python
s = {1, 2, 3, 4}

s.remove(2)     # Error if element not found
s.discard(10)   # No error if element not found
s.pop()         # Removes random element
s.clear()       # Removes all elements


---

# 🔹 Set Operations (Very Important)

Let:

python
A = {1, 2, 3}
B = {3, 4, 5}


## ✅ Union (All elements)

python
A | B
A.union(B)


Output:

{1, 2, 3, 4, 5}


---

## ✅ Intersection (Common elements)

python
A & B
A.intersection(B)


Output:

{3}


---

## ✅ Difference (Elements in A but not in B)

python
A - B
A.difference(B)


Output:

{1, 2}


---

## ✅ Symmetric Difference (Non-common elements)

python
A ^ B
A.symmetric_difference(B)


Output:

{1, 2, 4, 5}


---

# 🔹 Subset & Superset

python
A = {1, 2}
B = {1, 2, 3}

A.issubset(B)      # True
B.issuperset(A)    # True


---

# 🔹 Membership Test

python
if 2 in A:
    print("Yes")


Sets are faster than lists for membership checking.

---

# 🔹 Set Comprehension

python
squares = {x*x for x in range(5)}
print(squares)


---

# 🔹 Frozen Set (Immutable Set)

A *frozenset* is an immutable version of set.

python
fs = frozenset([1, 2, 3])


- Cannot add or remove elements
- Can be used as dictionary keys

---

# 🔹 Built-in Functions with Sets

python
len(A)
max(A)
min(A)
sum(A)


---

# 🔹 Time Complexity

| Operation | Time Complexity |
|------------|-----------------|
| Add | O(1) |
| Remove | O(1) |
| Membership Check | O(1) |
| Union | O(n) |
| Intersection | O(min(n, m)) |

---

# 🔹 When to Use Sets?

✅ Remove duplicates from a list  
✅ Fast membership testing  
✅ Mathematical set operations  
✅ Finding common elements  

---

# 🔹 Important Points

- Sets are implemented using hash tables.
- They do not maintain insertion order.
- They do not support indexing or slicing.
- Best for uniqueness and performance.

---

# 🎯 Summary

Use *Sets* when:
- You need unique values
- Order does not matter
- Fast lookup is required
