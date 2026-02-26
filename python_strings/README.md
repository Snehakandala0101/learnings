# 🔤 Python Strings 

This file contains my notes and practical examples on **Python strings**.

---

# Concepts & Definitions

A string is an immutable sequence of Unicode characters enclosed in:
- Single quotes (' ')
- Double quotes (" ")
- Triple quotes (''' ''' or """ """)

Strings are:
- Ordered
- Immutable
- Iterable

---

# 1️⃣ String Creation

Definition:
A string is an ordered collection of characters.

Example:
name = "Python"

---

# 2️⃣ String Indexing

Definition:
Accessing individual characters using position numbers.

Rules:
- Index starts from 0
- Negative indexing starts from -1 (last character)

Example:
s[0] → First character  
s[-1] → Last character

Time Complexity: O(1)

---

# 3️⃣ String Slicing

Definition:
Extracting a portion of a string using slicing.

Syntax:
string[start : stop : step]

Rules:
- start is inclusive
- stop is exclusive
- step controls increment
- step = -1 reverses the string

Slicing creates a new string (because strings are immutable).

---

# 4️⃣ String Immutability

Definition:
Strings cannot be modified after creation.

Example:
s[0] = 'P'  ❌ (Error)

Instead:
Create a new string.

---

# 5️⃣ Membership Operators

Definition:
Used to check if a substring exists inside a string.

Operators:
- in
- not in

Returns Boolean value.

---

# 6️⃣ String Methods

Definition:
Built-in functions used to manipulate and analyze strings.

String methods return a new string (they do not modify original string).

---

##  Case Conversion Methods

upper() → Converts string to uppercase  
lower() → Converts string to lowercase  
title() → Capitalizes each word  
capitalize() → Capitalizes first letter only  
swapcase() → Swaps uppercase to lowercase and vice versa  

---

## 🔹 Whitespace Removal Methods

strip() → Removes spaces from both ends  
lstrip() → Removes spaces from left  
rstrip() → Removes spaces from right  

---

## 🔹 Searching Methods

find(substring) → Returns index of first occurrence  
rfind(substring) → Returns last occurrence index  
index(substring) → Same as find but raises error if not found  
count(substring) → Counts occurrences (non-overlapping)

---

## 🔹 Replacement Methods

replace(old, new) → Replaces substring  

---

## 🔹 Splitting & Joining

split() → Converts string into list  
split(delimiter) → Splits using custom separator  
join(iterable) → Joins elements into string  

---

## 🔹 Checking Methods (Return Boolean)

isalpha() → Only letters  
isdigit() → Only digits  
isalnum() → Letters + numbers  
isspace() → Only whitespace  
islower() → All lowercase  
isupper() → All uppercase  

---

# 7️⃣ Escape Sequences

Definition:
Special characters used inside strings.

\n → New line  
\t → Tab  
\\ → Backslash  

---

# 8️⃣ String Formatting

Definition:
Inserting variables into strings dynamically.

Types:
- f-strings (Recommended)
- format()
- % formatting

---

# 9️⃣ Substring Searching

Definition:
Finding or counting occurrences of a substring inside a string.

Note:
count() does NOT count overlapping substrings.

To count overlapping substrings, manual slicing is required.

---

# 🔥 Important Interview Points

- Strings are immutable.
- Strings are stored in heap memory.
- Indexing is O(1).
- Slicing creates new object.
- count() ignores overlapping matches.
- Strings are iterable.
- Strings support negative indexing.

---