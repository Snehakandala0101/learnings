#function example
def greet(name):
    print(f"Hello {name}, welcome!")
greet("Sneha")

#square example
def square(n):
    return n*n
print(square(7))

#is_even(n) that returns true if the number is even otherwise false
def is_even(n):
    return n%2==0
print(is_even(22))
print(is_even(77))

#finding max of 3 numbers
def max_func(a,b,c):
    return max(a,b,c)
print(max_func(11,67,30))

#calculate factorial of a number
def cal_fact(n):
    if n==0:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
    return fact
print(cal_fact(5))
print(cal_fact(0))

#count vowels in a string
def vowel_count(text):
    vowels="aeiouAEIOU"
    count=0
    for char in text:
        if char in vowels:
            count+=1
    return count
print(vowel_count("hey user"))

#reverse string
def reverse(s):
    return s[::-1]
print(reverse("VSCode"))

#prime number check
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
print(is_prime(9))
print(is_prime(11))

#sum of elements in a list
def sum_of_ele(list):
    sum=0
    for i in list:
        sum+=i
    return sum
list=[1,2,3,4,5,6,7,8,9]
print(sum_of_ele(list))

    










