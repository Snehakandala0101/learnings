# 📘 Lists in Python

## 🔹 Definition

A *List* is an ordered, mutable collection of elements in Python.

- Lists are written using square brackets []
- Lists allow duplicate values
- Lists can store multiple data types

python
numbers = [1, 2, 3, 4]
names = ["John", "Emma", "John"]
mixed = [1, "Sneha", 3.5, True]


---

# 🔹 Key Properties of Lists

| Property | Description |
|-----------|------------|
| Ordered | Elements maintain insertion order |
| Mutable | Can modify, add, remove elements |
| Duplicates | Allowed |
| Indexed | Supports positive & negative indexing |
| Dynamic | Can grow or shrink in size |

---

# 🔹 Creating Lists

python
# Empty list
empty_list = []

# Using list constructor
nums = list((1, 2, 3))

# List with different data types
data = [10, "Python", 3.14]


---

# 🔹 Accessing Elements

python
numbers = [10, 20, 30, 40, 50]

numbers[0]     # First element → 10
numbers[-1]    # Last element → 50
numbers[1:4]   # Slicing → [20, 30, 40]


---

# 🔹 Updating List

python
numbers = [10, 20, 30]
numbers[1] = 99

print(numbers)
# Output: [10, 99, 30]


---

# 🔹 Adding Elements

python
nums = [1, 2, 3]

nums.append(4)        # Add at end
nums.insert(1, 10)    # Insert at index

print(nums)


---

# 🔹 Removing Elements

python
nums = [1, 2, 3, 4, 5]

nums.remove(3)   # Removes value 3
nums.pop()       # Removes last element
nums.pop(1)      # Removes element at index 1
nums.clear()     # Removes all elements


---

# 🔹 Important List Methods

| Method | Purpose |
|---------|--------|
| append() | Add element at end |
| insert() | Insert at specific index |
| remove() | Remove specific value |
| pop() | Remove element by index |
| clear() | Remove all elements |
| sort() | Sort list |
| reverse() | Reverse list |
| count() | Count occurrences |
| index() | Find position |

Example:

python
nums = [4, 2, 1, 3]

nums.sort()
nums.reverse()
print(nums)


---

# 🔹 Looping Through List

python
numbers = [1, 2, 3]

for num in numbers:
    print(num)


Using index:

python
for i in range(len(numbers)):
    print(numbers[i])


---

# 🔹 List Slicing

python
nums = [0, 1, 2, 3, 4, 5]

nums[1:4]     # [1, 2, 3]
nums[:3]      # [0, 1, 2]
nums[3:]      # [3, 4, 5]
nums[::-1]    # Reverse list


---

# 🔹 Nested Lists

python
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[0][1])  # Output: 2


---

# 🔹 List Comprehension (Short Way)

python
squares = [x*x for x in range(1, 6)]
print(squares)


With condition:

python
evens = [x for x in range(10) if x % 2 == 0]


---

# 🔹 Built-in Functions with List

python
nums = [10, 20, 30]

len(nums)
max(nums)
min(nums)
sum(nums)


---

# 🔹 Time Complexity

| Operation | Time Complexity |
|------------|-----------------|
| Access by index | O(1) |
| Append | O(1) |
| Insert | O(n) |
| Remove | O(n) |
| Search | O(n) |

---

# 🔹 When to Use List?

✅ When order matters  
✅ When you need to modify data  
✅ When duplicates are allowed  
✅ When indexing is required  

---

# 🔹 Important Points

- Lists are implemented as dynamic arrays.
- They store references to objects.
- Faster access using index.
- Slower insertion/deletion in middle.

---

# 🎯 Summary

A List is best used when:
- You need ordered data
- You need to modify elements
- You want flexibility
