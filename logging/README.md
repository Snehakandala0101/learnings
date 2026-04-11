# Logging in Python

---
## Logging

Logging is a built-in Python feature used to:
+ Track program execution
+ Record errors
+ Debug applications
+ Monitor production systems

It is more powerful and professional than using ```print()``` statements.

---
### Why Logging Instead of Print?
print()	|logging|
|:-----|:----|
Used for simple output|	Used for tracking & debugging
No severity levels|	Has log levels
Cannot store history easily|	Can write to files
Not suitable for production	|Used in real-world applications|
---
## Logging Levels

Logging provides different severity levels:

1. **DEBUG** → Detailed information (variable values)
2. **INFO** → General program flow
3. **WARNING** → Something unexpected but program continues
4. **ERROR** → Serious issue (program part fails)
5. **CRITICAL** → Major failure (program may stop)

**Order of severity:**

```DEBUG < INFO < WARNING < ERROR < CRITICAL```

---
### Basic Logging Setup

To configure logging:
- Set logging level
- Define log message format
- Choose where logs are stored (console or file)

**Example components:**

- Logger
- Handler
- Formatter
---
#### Important Components
1. **Logger**

Responsible for generating log messages.

Example:
```getLogger()```

2. **Handler**

Decides where logs go:
+ Console → StreamHandler
+ File → FileHandler
+ Rotating files → RotatingFileHandler

3. **Formatter**

Defines structure of log message.

**Common format fields:**
* %(asctime)s → Timestamp
* %(levelname)s → Log level
* %(message)s → Actual message
---
### Logging to a File

To store logs in a file:
* Use FileHandler
* Set level
* Attach formatter
* Add handler to logger

This is useful for:
* Login systems
* Payment systems
* Backend APIs
* Production debugging
---
#### Multiple Handlers

You can create:
- One file for INFO logs
- One file for ERROR logs

Each handler can have:
- Different level
- Different file
- Same logger

This is called **advanced logging configuration.**
practice Implementation:[View Code](./multiple_handlers/multiplehandlers.py)

---
#### Exception Logging

Instead of just logging error messages, you can log full traceback using:
```logger.exception()```
This helps in debugging real applications.

---
### Logging in Real-World Projects

Logging is commonly used in:
- Login systems
- Order processing systems
- Banking systems
- Backend APIs
- AI model monitoring
- Production servers
---
#### Best Practices

:heavy_check_mark: Do not use print in production
:heavy_check_mark: Use appropriate log level
:heavy_check_mark: Do not log sensitive data (passwords)
:heavy_check_mark: Use separate files for errors in large systems
:heavy_check_mark: Always include timestamp

---
#### Logging vs File Handling
- File handling → Manually reading/writing files
- Logging → Automatically recording program events

Logging internally uses file handling but is considered a separate concept.

---
🔹 Summary

Logging is:

A debugging tool
A monitoring system
A production requirement
A professional coding practice

It is essential for backend development and real-world software systems.