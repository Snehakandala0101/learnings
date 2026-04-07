# Abstraction in Python
---

**Abstraction** is a core concept of Object-Oriented Programming (OOP) that allows a programmer to hide internal details and show only essential features to the user.
* Focuses on what an object does, not how it does it.
* Makes code cleaner, easier to manage, and less complex.
* In Python, abstraction is implemented using:
    * Abstract Classes
    * Abstract Methods
---
### Purpose of Abstraction
+ Reduce Complexity: Hide unnecessary details from the user.
+ Enhance Security: Prevent direct access to implementation details.
+ Promote Reusability: Abstract classes can be reused as a blueprint.
+ Support Polymorphism: Different subclasses can implement abstract methods differently.
---
## Abstract Class
An abstract class is a class that cannot be instantiated.
It can contain:
- Abstract methods (must be implemented by subclasses)
- Concrete methods (optional, with actual implementation)

**Syntax:**
```python
from abc import ABC, abstractmethod

class AbstractClassName(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
```
---
## Abstract Method
- A method without implementation in the abstract class.
- Must be overridden by any concrete subclass.
- Declared using the @abstractmethod decorator.

**Example:**`
```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```
---
## Implementing Abstraction

**Step 1:** Create an abstract class with abstract methods.
**Step 2:** Create a subclass that implements all abstract methods.
**Step 3:** Instantiate the subclass and use its methods.

---
#### Key Points
:bulb: Abstraction hides implementation details.
:bulb: Abstract classes cannot be instantiated directly.
:bulb: Abstract methods must be implemented in concrete subclasses.
:bulb: Can have regular (concrete) methods alongside abstract methods.
:bulb: Python uses the abc module (```ABC class``` and ```@abstractmethod```) for abstraction.

---
### Advantages of Abstraction
| Advantage|	Description|
|:---------|:----------|
|Hides complexity|	User interacts only with essential features.|
|Improves maintainability|	Changes in internal implementation won’t affect users.|
| Promotes code reusability	|Abstract classes act as blueprints for multiple subclasses.|
| Supports polymorphism|	Same method can have different behavior in different subclasses.|
|Enhances security	|Internal logic is hidden from direct access.|
---
### Types of Abstraction in Python
1. **Full Abstraction**
All methods are abstract.
Example: An abstract class with only abstract methods.
2. **Partial Abstraction**
Contains both abstract and concrete methods.
Example: Vehicle class may have a concrete method like fuel_type() alongside abstract methods.

---
### Real-world Examples
:heavy_plus_sign: **TV Remote:**
You press buttons (interface) → TV responds (implementation hidden)
:heavy_plus_sign: **Bank ATM:**
You enter PIN and withdraw money → internal processes hidden
:heavy_plus_sign: **Vehicle Dashboard:**
Speedometer shows speed → engine mechanics hidden

---
### Abstraction vs Encapsulation
|Feature	|Abstraction	|Encapsulation|
|:----------:|:-------------:|:------------|
|Definition|	Hides internal implementation|	Hides internal data|
|Focus|	What an object does	|How data is stored and accessed
|Implementation|	Abstract classes and methods	|Access modifiers (private, protected)|
|Goal	|Reduce complexity|	Protect data|

---
