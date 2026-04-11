# PYTHON JSON 
---
## JSON
JSON (**JavaScript Object Notation**) is a lightweight text-based data format used to store and exchange structured data.
It is:
- Human-readable
- Machine-readable
- Language independent
- Widely used in web applications and APIs

:pushpin: Even though it comes from JavaScript, it is used in Python, Java, C++, etc.

---
### Why Do We Need JSON?

Before JSON:
+ Data was stored in XML (complex and heavy)
+ Data exchange was harder

JSON solved this because:
+ Simple structure
+ Easy to parse
+ Lightweight
+ Faster for web communication

Today:
+ Almost all REST APIs return JSON
+ Frontend and backend communicate using JSON

---
### Basic JSON Structure

JSON stores data in:

:small_blue_diamond: Objects → ```{ }```

Key-value pairs
```JSON
{
  "name": "Sneha",
  "age": 22
}
```
:small_blue_diamond: Arrays →``` [ ]```

Ordered list of values
```JSON
{
  "skills": ["Python", "Java", "SQL"]
}
```
---
#### JSON Data Types

JSON supports only 6 data types:

|Type|	Example|
|:-----:|:------|
String	|```"name": "Sneha"```
Number	|```"age": 22```
Boolean	|```"isStudent": true```
Array	|```"marks": [80, 90, 85]```
Object	|```"address": {"city": "Hyd"}```
Null	|```"middleName": null```

---

### JSON Rules (Very Important)
1. Keys must be in double quotes
2. Strings must use double quotes
3. No trailing comma allowed
4. Data must be valid structure
5. Case sensitive

:x: Invalid:
```JSON
{
  name: "Sneha"
}
```
:heavy_check_mark: Valid:
```JSON
{
  "name": "Sneha"
}
```
---
#### JSON vs Python Dictionary
JSON	|Python|
|:------:|:-----:|
true	|True
false	|False
null	|None
Only double quotes|	Single or double allowed

Example:

JSON:
```JSON
{
  "isStudent": true
}
```
Python:
```python
{"isStudent": True}
```
---
### Working with JSON in Python

Import module:
```python
import json
```
---
:small_blue_diamond: **JSON → Python (Reading)**
```python
data = json.load(file)
```
Converts JSON file into Python dictionary.

---
:small_blue_diamond: **Python → JSON (Writing)**
```python
json.dump(data, file)
```
Writes Python dictionary into JSON file.

---
:small_blue_diamond: **String Conversion**

Python → JSON string:
```python
json_string = json.dumps(data)
```
JSON string → Python:
```python
python_obj = json.loads(json_string)
```
---

Function|	Use|
|:-----:|:-----|
dump()|	Write to file
dumps()|	Convert to string
load()|	Read from file
loads()|	Convert from string

---
##### Nested JSON 

Example:
```JSON
{
  "company": "TechSoft",
  "employees": [
    {
      "name": "John",
      "department": "IT"
    }
  ]
}
```
Structure understanding:

Dictionary
→ key "employees"
→ value is List
→ inside list = Dictionary

To access department:
```python
data["employees"][0]["department"]
```
Understanding nesting is the most important skill.

---
##### Reading JSON
1. Open file
2. Convert JSON → Python object
3. Modify data
4. Convert Python → JSON
55. Save back to file

This is how:
- Inventory systems work
- Login systems work
- Configuration systems work

---
#### Updating JSON Data

Steps:
- Loop through list
- Match condition
- Update dictionary value
- Write back to file

Example logic:
```python
for product in data["products"]:
    if product["name"] == input_name:
    product["quantity"] = new_value
```
--- 
##### Common Errors
:x: **FileNotFoundError**
File path wrong
:x: **JSONDecodeError**
Invalid JSON format
:x: **KeyError**
Key doesn’t exist
:x: **TypeError**
Wrong data type

---
#### Exception Handling with JSON
```python
try:
    with open("file.json") as file:
        data = json.load(file)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON format")
```
---
#### Real World Applications
- REST APIs
- Web development (Frontend ↔ Backend)
- Storing user data
- Login systems
- Product inventory
- Configuration files
- Microservices communication

---
#### :bulb:Key Concept to Always Remember

JSON is just structured text.

When working in Python:

- Object → Dictionary
- Array → List

Before coding:
👉 Always understand the structure first.

---
###### Summary

JSON = Data format
Python = Programming language
json module = Bridge between them

You read → modify → write back.
