# Python Internals & Execution model


This folder contains my structured experiments and notes on Python Internals,including execution model,memory management,bytecode,and practical examples.

---
## Summary of key concepts

### Python Execution Model
Python executes the code in the following pipeline:

#### python execution flow(ASCII)
         Source Code (.py)
              |
              v
          Tokenizing
              |
              v
             AST
              |
              v
        Bytecode Compilation
              |
              v
        PVM Execution



### Memory Management

Stack: Stores function calls and local variables
Heap: Stores objects (lists, dicts, class instances)
Reference Counting: Frees objects when reference = 0
Garbage Collection: Cleans circular references 

### Variable Binding

Variables are references to objects, not containers of values.
Modifying one reference affects all references to that object.

---

#### Full Detailed notes
For a complete set of notes for these topics ,see:
[(python_internals_notes)](Notes/python_internals_notes.md)



