#global scope and local scope
x = 10
def func():
    x = 5
    print(x)  # prints local variable 5
func()
print(x) #prints the global variable i.e., 10


#changing global variable
x = 10
def func():
    global x
    x = 20
func()
print(x)   #global variable 10 is chamged to 20 by using global keyword .so it prints 20

#local scope example
def func():
    y = 5
    print(y)  # prints 5(local variable)
func()
print(y)  # gives name error ,as the local variable cannot be accessed outside the function

