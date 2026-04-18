#simple decorator example
def my_decorator(func):
    def wrapper():
        print("Starting....")
        func()
        print("Finished!")
    return wrapper

@my_decorator
def greet():
    print("Hello")
greet()


#multiply return value
def multiply_by_10(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)*10
        return result
    return wrapper
@multiply_by_10
def get_number():
    return 5
print(get_number())




# count function calls
def count_calls(func):
    count=0
    def wrapper():
        nonlocal count
        func()
        count+=1
        print(f"Function called {count} times")
    return wrapper
@count_calls
def say_hi():
    print("Hi")
say_hi()
say_hi()
say_hi()
say_hi()



#validate positive numbers
def validate_positive(func):
    def wrapper(*args,**kwargs):
        for value in args:
            if value<0:
                return "Invalid Input"
            return func(*args,**kwargs)
    return wrapper
@validate_positive
def add(a,b):
    return a+b
print(add(2,3))



#decorators with arguments
#repeat n times
from functools import wraps
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(n):
                result=func(*args,**kwargs)
            return result
        return wrapper
    return decorator
@repeat(4)
def greet():
    print("Hi")
greet()



#permission role decorator
from functools import wraps
def require_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(self,*args,**kwargs):
            if self.role == required_role:
                return func(self,*args,**kwargs)
            else:
                return "Access denied"
        return wrapper
    return decorator
class type_of_user:
    def __init__(self,role):
        self.role=role
    @require_role("admin")
    def delete_user(self):
        return "User deleted"
    
admin=type_of_user("admin")
user=type_of_user("user")
print(admin.delete_user())  
print(user.delete_user())


#return list of results
from functools import wraps
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            results=[]
            for i in range(n):
                res=func(*args,**kwargs)
                results.append(res)
            return results
        return wrapper
    return decorator
@repeat(3)
def square(x):
    return x * x
print(square(4))



# simple logging decorator

def log_execution(func):
    def wrapper(*args,**kwargs):
        print("Calling function: ",func.__name__)
        result=func(*args,**kwargs)
        print("Arguments passed ",args,kwargs)
        print("Function returned ",result)
        return result
    return wrapper
@log_execution
def add(a, b):
    return a + b

print(add(3, 5))
