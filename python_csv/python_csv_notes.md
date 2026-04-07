# Python CSV Notes
---
## CSV

CSV (**Comma Separated Values**) is a simple file format used to store tabular data like:
- Excel data
- Student records
- Employee details
- Sales reports

**Example:**
```csv
name,age,marks
Sneha,21,90
Ravi,22,85
```

Each line = row
Each value separated by comma = column

---
### Why Use CSV in Python?
* Lightweight and simple
* Human readable
* Easily supported by Excel
* Used in data analysis and backend systems
* Good for storing structured data

---
### CSV Module in Python

Python provides a built-in module called:
```python
import csv
```
Used for:
- Reading CSV files
- Writing CSV files
- Updating records

---
### :book:Reading CSV Files
1. **Using ```csv.reader()```**

Reads file row by row as a list.
```python
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

:diamonds: Output format:
```python
['name', 'age', 'marks']
['Sneha', '21', '90']
```
Each row is a list.

2. **Using ```csv.DictReader()```**

Reads rows as dictionary.
```python
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["marks"])
```
:diamonds: Output format:
```python
{'name': 'Sneha', 'age': '21', 'marks': '90'}
```
Each row is a dictionary (column name = key).
:white_check_mark: Preferred in real projects because it is more readable.

---
### :writing_hand:Writing CSV Files
1. **Using ```csv.writer()```**
```python
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "marks"])
    writer.writerow(["Sneha", 21, 90])
```
⚠ Why ```newline=""```?

Without it:
- Extra blank lines appear in Windows

2. **Using ```csv.DictWriter()```**
```python
import csv

fieldnames = ["name", "age", "marks"]

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "Sneha", "age": 21, "marks": 90})
```
Best for structured data handling.

---
### :pushpin: Append Data to CSV
```python
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Ravi", 22, 85])
```
Mode ```"a"``` → append mode

---
### :pushpin: Updating or Deleting Records

CSV does not support direct update/delete.

Steps:
- Read all data
- Modify in memory
- Rewrite entire file

Example logic:
```python
rows = []

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] != "Ravi":
            rows.append(row)

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
```
---
#### CSV vs JSON
CSV |	JSON|
|:-----:|:---:|
Tabular data|	Structured data
Simple format	|More flexible
Less hierarchical|	Supports nested data
Used in Excel|	Used in APIs|

---
#### Common Errors in CSV
1. **FileNotFoundError**
Occurs if file does not exist.
2. **ValueError**
If converting string to int fails.
3. **Extra Blank Lines**
Solved by using:
```newline=""```
---
##### Real World Use Cases
- Attendance system
- Student result system
- Employee payroll system
- Sales tracking
- Data preprocessing for ML
---
##### Best Practices
:heavy_check_mark: Always use with open()
:heavy_check_mark: Use DictReader() for clarity
:heavy_check_mark: Convert numeric values properly
:heavy_check_mark: Handle exceptions
:heavy_check_mark: Keep backup before rewriting file