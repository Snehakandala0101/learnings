tuple=(1,5,3,7,2,9,10)

#length of the tuple without using len()
count=0
for i in tuple:
    count+=1
print(count)

#check whether the number is in tuple or not
print(0 in tuple)

#max,min and sum
print(max(tuple))
print(min(tuple))
print(sum(tuple))

#merging
tuple1=(1,2,3,4,5)
tuple2=(6,7,8,9)
tuple3=tuple1 +tuple2
print(tuple3)

#unpacking example
x=(10,20,30)
x1,x2,x3=x
print(x1)
print(x2)
print(x3)

#swapping two variablles using tuple unpacking
t=(11,22)
t1,t2=t
t1,t2=t2,t1
print(t1)
print(t2)

#accessing the elements 
z=(1,(2,3),4)
print(z[1][1])