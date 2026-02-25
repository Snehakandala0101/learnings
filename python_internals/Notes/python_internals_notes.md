# 🐍 Python Internals – Key Notes

These notes summarize my learning journey on Python internals, including execution model, memory management, bytecode, and variable behavior.  
For all runnable code examples, see the corresponding practice files in this folder.

---

## 1️⃣ Python Execution Model

Python code executes in the following pipeline:
Source Code (.py) → Tokenizing → AST → Compilation (Bytecode) → Python Virtual Machine (PVM)


- *Tokenizing:* Breaks code into meaningful tokens (keywords, identifiers, operators).  
- *AST (Abstract Syntax Tree):* Logical representation of code.  
- *Bytecode:* Platform-independent intermediate code executed by PVM.  
- *PVM (Python Virtual Machine):* Stack-based interpreter that executes bytecode instructions.

*Example snippet:*  

For a function execution demonstration, see [practice](../practice.py)
---

## 2️⃣ Memory Management

Python memory is divided into *Stack* and *Heap*:

### Stack
- Stores function calls and local variables  
- Automatically managed, fast access  

### Heap
- Stores dynamically created objects (lists, dicts, class instances)  
- Managed by Python’s memory manager  

### Reference Counting
- Python tracks the number of references to each object  
- When the reference count reaches zero → memory is freed  

### Garbage Collection
- Handles circular references that reference counting alone cannot free  

*Demonstration:*  
See [memory_examples](../memory_ex.py) for examples of stack vs heap, reference counts, and circular reference cleanup.

---

## 3️⃣ Variable Binding

- Variables in Python are *references to objects*, not containers of values  
- Multiple variables can reference the same object; modifying via one affects all  

*Practice:*  
Check [memory_examples](../memory_ex.py#L15-L20) for variable binding examples.

---

## 4️⃣ Bytecode Exploration

- Python’s dis module converts functions into *bytecode instructions*  
- Key instructions: LOAD_FAST, LOAD_CONST, BINARY_OP, RETURN_VALUE  
- Helps understand *Python’s internal execution*  

*Try it:*  
See [bytecode_examples](../bytecode_examples.py) for function bytecode examples.

---

## 5️⃣ Stack vs Heap

- *Stack:* Holds function calls and local variables  
- *Heap:* Stores dynamically created objects  

*Visualization:*  
See [memory_examples](../memory_ex.py#L5-L25) for practical examples and object IDs.

---

## 6️⃣ Insights & Tips

- Python is both *compiled (to bytecode) and interpreted (by PVM)*  
- Script mode executes the entire file; interactive mode executes line by line  
- Small integers (-5 to 256) are cached  
- Reference counting + garbage collection avoids memory leaks  
- dis.dis() and sys.getrefcount() are your friends for exploring internals  
- Understanding internals improves *backend performance and debugging skills*

---

