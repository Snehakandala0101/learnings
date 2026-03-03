#removing duplicates
s=[1,2,3,4,4,5,5]
s1=set(s)
print(s1)

#unique characters
a='python'
b='apple'
if len(a)==len(set(a)):
    print("true")
else:
    print("false")
if len(b)==len(set(b)):
    print('true')
else:
    print('false')


#count unique elements
c=[1,2,3,3,4,4,5,5,1,2]
c1=set(c)
print(len(c1))

#common  elements
d={1,2,3,4}
e={3,4,5,6}
print(d & e)

#union of two sets
print(d.union(e))


#subset check
f1={"python","c","java","cpp"}
f2={"cpp","c","javascript"}
print(f2.issubset(f1))

#symmetric difference
print(f2.symmetric_difference(f1))


#finding the firts repeating element
numbers=[4,5,6,4,3,2,3]
seen=set()
for num in numbers:
    if  num in seen:
        print(num)
        break
    seen.add(num)

#remove elements greaater than 10
sets={5,12,7,18,3,25}
sets={set for set in sets if set<10}
print(sets)

#sort()
x={2,5,3,7,8,1}
print(sorted(x)) #built-in function


#finding duplicates 
y=[2,3,5,7,1,2,9,9]
seen=set()
duplicates=set()
for num in y:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print(duplicates)

#finding longest consecutive sentence
input={100,4,200,1,3,2}
longest=0
for num in input:
    if num-1 not in input:
        current=num
        length=1
        while current+1 in input:
            current+=1
            length+=1
        longest=max(longest,length)
print(longest)

#power set size(if a set has n elements ,then power set size is 2^n)
size=2**len(input)
print(size)

#frozen set( an immutable version of set)
my_set=frozenset([1,2,3,4])
print(my_set)

#remove intersection from both the sets
set1={1,2,3,4,5,6,7}
set2={5,6,7,8,9,10}
set3=set1.symmetric_difference(set2)
print(set3)







