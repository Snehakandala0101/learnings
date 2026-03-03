# 📘 Python Data Structures – Complete Notes & Practice
 
This project contains structured notes, examples, and practice programs for core Python data structures.

---

# 📂 Folder Structure


python_data_structures/
│
├── dictionary/
│    ├── dictionary_notes.md
│   └── dictionary.py
│
├── list/
│   ├── list_notes.md
│   └── list.py
│
├── set/
│   ├── set_notes.md
│   └── sets.py
│
├── tuple/
│   ├── tuple_notes.md
│   └── tuple.py
│
├── README.md


---

# 📚 Topics Covered

- ✅ Lists
- ✅ Tuples
- ✅ Sets
- ✅ Dictionaries

Each topic includes:

- 📘 Detailed theory notes
- 🧠 Practice problems
- 📊 important points
- ⏱ Time complexity analysis

---

# 📊 Comparison of Data Structures

| Feature | List | Tuple | Set | Dictionary |
|----------|------|--------|------|------------|
| Syntax | [] | () | {} | {key: value} |
| Ordered | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes (Python 3.7+) |
| Mutable | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Duplicates | ✅ Allowed | ✅ Allowed | ❌ Not Allowed | ❌ Keys Not Allowed |
| Indexing | ✅ Yes | ✅ Yes | ❌ No | ❌ No (Access by key) |
| Use Case | Sequence of items | Fixed data | Unique values | Key-value mapping |
| Performance | Fast index access | Faster than list | Fast membership | Fast lookup |

---

# ⏱ Time Complexity Comparison

| Operation | List | Tuple | Set | Dictionary |
|------------|--------|--------|------|------------|
| Access | O(1) | O(1) | ❌ | O(1) |
| Search | O(n) | O(n) | O(1) | O(1) |
| Insert | O(n) | ❌ | O(1) | O(1) |
| Delete | O(n) | ❌ | O(1) | O(1) |

---

# 🎯 When to Use What?

| Scenario | Best Choice |
|-----------|------------|
| Ordered & modifiable data | List |
| Fixed & unchangeable data | Tuple |
| Removing duplicates | Set |
| Fast key-based lookup | Dictionary |
| Creating compact lists | List Comprehension |

---

# 🔥 Focus Points

- Lists are dynamic arrays.
- Tuples are immutable and slightly faster.
- Sets use hashing for fast lookup.
- Dictionaries use hash tables internally.
- get() method prevents key errors.
- Membership testing is fastest in sets & dictionaries.


---

👩‍💻 Maintained by: Sneha Kandala  