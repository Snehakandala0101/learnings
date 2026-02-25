import dis
def add(a,b):
    return a+b

def check_even(n):
    if n%2==0:
        return "even"
    return "odd"

def loop_example():
    total=0
    for i in range(3):
        total+=i
    return total
print("\n---Bytecode:add---")
dis.dis(add)
print("\n---Bytecode:check_even---")
dis.dis(check_even)
print("\n---Bytecode:loop_example---")
dis.dis(loop_example)