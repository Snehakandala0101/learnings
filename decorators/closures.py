# simple memory function

def outer():
    message="Python"

    def inner():
        print(message)
    return inner
func=outer()
func()

#personalized greeting
def greeting(name):

    def inner_greet():
        print(f"Hello {name}")
    return inner_greet
greet_sneha=greeting("Sneha")
greet_sneha()

#power function
def power(n):
    def multiply(x):
        return x**n
    return multiply
square=power(2)
cube=power(3)
powerfive=power(5)
print(square(4))
print(cube(2))
print(powerfive(2))

#counter function
def counter():
    count=0
    def counter_c():
        nonlocal count    #Looks for 'count' variable in the nearest enclosing scope.
        count+=1
        print(count)
    return counter_c
c1=counter()
c2=counter()
c1()
c1()
c2()

#multiply with validation
def multiplier(n):
    def inner(x):
        if x>0:
            return x*n
        else:
            return "Invalid input"
    return inner
double=multiplier(2)
print(double(5))
print(double(-3))

#independent closures
def test():
    x=10
    def inner():
        print(x)
    return inner
a=test()
b=test()
a()
b()
