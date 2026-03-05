# *args example
def sum(*numbers):
    sum=0
    for i  in numbers:
        sum+=i
    return sum
print(sum(1,2,3,4,5))
print(sum(11,22,4,5,3))

#largest number
def max_value(*nums):
    return max(nums)
print(max_value(0,7,8,2,4,66))
print(max_value(100,900,300))

#function that prints all arguments given
def show_items(items):
    for i in items:
        print(i)
items=("apple","banana","cherry")
show_items(items) 

#kwargs example
def person(**details):
    print(details)
person(name="sneha",age=22,city="Hyderabad")

#checking using keywords
def check(**data):
    return data["age"]
print(check(age=25, name="Rahul"))

#function that prints only values
def display(**profile):
    for value in profile.values():
        print(value)
display(name="sneha",role="Engineer")

#positional and keyword arguments example
def student_info(name,*marks,**details):
    print("Name: ",name)
    print("Marks:",marks)
    print("Details:",details)
student_info("Sneha",90,85,88,city="Hyderabad",course="Python")