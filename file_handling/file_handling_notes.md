# Python File Handling
---
### File Handling

File handling in Python allows us to:
- Create files
- Open files
- Read data from files
- Write data to files
- Append data
- Close files

It is used to store data permanently instead of temporary memory (RAM).

---
### Why File Handling is Important?
* Store user data
* Save logs
* Maintain reports
* Store configuration
* Work with datasets (CSV, JSON)
* Build real-world applications

---
#### Opening a File
**Syntax**
file_object = open("filename", "mode")
**Example**
```python
f = open("data.txt", "r")
```
---
#### File Modes
|Mode|	Description|
|:-----:|:--------|
r|	Read mode (default). File must exist.
w	|Write mode. Creates file if not exists. Overwrites existing data.
a	|Append mode. Adds data at the end.
x	|Create mode. Error if file already exists.
rb	|Read binary mode (images, pdf, etc.)
wb	|Write binary mode|

---
##### Reading from a File
1️⃣ **read()**

Reads entire file content.
```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```
2️⃣ **readline()**

Reads one line at a time.
```python
with open("data.txt", "r") as f:
    print(f.readline())
```
3️⃣ **readlines()**

Returns all lines as a list.
```python
with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)
```
---
##### Writing to a File
**write()**

Writes data into file.
```python
with open("data.txt", "w") as f:
    f.write("Hello Python\n")
```
⚠️ Note:

- write() does NOT add newline automatically.
- Use \n manually.
---
##### Append Mode

Adds data without deleting old content.
```python
with open("data.txt", "a") as f:
    f.write("New line added\n")
```
---
##### Closing a File

**Manual closing:**
```python
f = open("data.txt", "r")
f.close()
```
But **recommended way is using ```with``` statement.**

**Best Practice – Using ```with```**
```python
with open("data.txt", "r") as f:
    print(f.read())
```
---
###### Advantages:
- Automatically closes file
- Cleaner and safer
- Prevents memory leaks
---
### File Pointer

Every file has a pointer that tracks current position.
1. **tell()**

Returns current position.
```python
f.tell()
```
2. **seek()**

Moves pointer to specific position.
```python
f.seek(0)
```
---
#### Checking if File Exists
```python
import os

if os.path.exists("data.txt"):
    print("File exists")
```
---
#### Deleting a File
```python
import os
os.remove("data.txt")
```
---
### Binary File Handling

Used for:
- Images
- Videos
- PDFs
```python
with open("image.jpg", "rb") as f:
    data = f.read()
```
---
### Exception Handling in File Handling

Common errors:

- FileNotFoundError
- PermissionError
- IOError

**Example:**
```python
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
```