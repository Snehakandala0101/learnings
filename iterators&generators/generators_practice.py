#simple number genertor
def number(n):
    num=1
    while num<=n:
        yield num
        num+=1
values=number(10)
for value in values:
    print(value)

#even number generator 
def even_num(n):
    for i in range(n+1):
        if i%2==0:
            yield i
evennumbers=even_num(30)
for evennumber in evennumbers:
    print(evennumber)


#even number generator without  using range()
def even_number(n):
    num=2
    while num<=n:
        yield num
        num+=2
evennumbers=even_number(30)
for evennumber in evennumbers:
    print(evennumber)

#square generator
def square_num(n):
    num=1
    while num<=n:
        sq=num*num
        yield sq
        num+=1
sq_numbers=square_num(20)
for sq_number in sq_numbers:
    print(sq_number)

#reverse string generator
def rev_string(orig_string):
    str_len=len(orig_string)-1
    while str_len>=0:
        reverse=orig_string[str_len]
        yield reverse
        str_len-=1
for ch in rev_string("Python"):
    print(ch)

#fibonacci generator
# 0 1 1 2 3 5 8 13 21...
def fibonacci_num(n):
    first_num=0
    sec_num=1
    for i in range(n+1):
        yield first_num
        first_num,sec_num=sec_num,first_num+sec_num  #tuple unpacking
for num in fibonacci_num(5):
    print(num)

#countdown generator
def count_down(n):
    while n>=0:
        yield n
        n-=1
for num in count_down(5):
    print(num)

#prime numbers generator
#2 3 5 7 11 13 17 19 22 23 27
def prime_num(n):
    for num in range(2,n+1):
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            yield num
for prime in prime_num(20):
    print(prime)

#custom range generator
def custom_range(start,stop,step):
    while start<stop:
        yield start
        start+=step
for num in custom_range(2,20,3):
    print(num)
