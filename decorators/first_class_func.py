#function assigner
def say_hi():
    print("Hi!")
my_func=say_hi
my_func()

#function list
def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
#storing functions in list
operations=[add,subtract,multiply]
for operation in operations:
    operation(10,5)

#function dictionary
def circle_area(r):
    area=3.14*r*r
    return area
def square_area(side):
    area=side*side
    return area
shapes={
    "circle":circle_area,
    "square":square_area
}
choice=input("enter you choice")
if choice in shapes:
    value=float(input("enter the value: "))
    result=shapes[choice](value)
    print("Area is: ",result)
else:
    print("Invalid shape")

#custom message formatter
def process_text(func,text):
    return func(text)
def make_upper(text):
    return text.upper()
def make_lower(text):
    return text.lower()
def add_exclamation(text):
    return text+"!"

operations = {
    "upper": make_upper,
    "lower": make_lower,
    "exclaim": add_exclamation
}

choice=input("enter the format you want ")
text=input("enter the text: ")

if choice in operations:
    result=process_text(operations[choice],text)
    print("Result: ",result)
else:
    print("invalid format")



