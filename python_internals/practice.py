import dis
import sys
import gc

# simple function
def multiply(a,b):
    return a*b
print("result= ",multiply(5,3))

# bytecode inspection
print("\nBytecode of multiply: ")
dis.dis(multiply)

#variable binding
x=10
y=x
print("\n Variable Binding:" )
print("id(x):",id(x))
print("id(y):",id(y))

#reference counting
print("\n Reference Count of x:")
print(sys.getrefcount(x))

#circular reference example
print("\nCreating circular reference:")
a=[]
b=[a]
a.append(b)

del a
del b

gc.collect()
print("Garbage collection Completed")