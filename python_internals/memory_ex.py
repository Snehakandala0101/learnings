#stack example
def greet(name):
    message=f"hello {name}"
    return message
print(greet("sneha"))

#heap example
my_list=[1,2,3]
print("LIST ID:",id(my_list))

#small integer caching
a=10
b=10
print("small integer caching IDs:",id(a),id(b))


#Large integer caching
a=10000
b=10000
print("large integer caching IDs:",id(a),id(b))
