list=[1,2,3,4,5,6,7]
#list length
print(len(list))

#list length without using len()function
count=0
for num in list:
    count+=1
print(count)

#sum of elements
sum=sum(list)
print(sum)

#sum with using sum() function
sum=0
for num in list:
    sum+=num
print(sum)

#maximum and minimum
print(max(list))
print(min(list))

#maximum and minimum without using max() and min() functions
print("min =",[num for num in list if num-1 not in list])
print("max= ",[num for num in list if num+1 not in list])

#reverse a list without using reverse() and slicing
#using a new list 
my_list=[]
for i in range(len(list)-1,-1,-1):   #range(start,stop,step)
    my_list.append(list[i])
print(my_list)

#using swap method
start=0
end=len(list)-1
while start<end:
    list[start],list[end] = list[end],list[start]
    start+=1
    end-=1
print(list)

#removing duplicates by maintaing the order
list1=[1,2,4,5,7,1,3,4,2,4,5,7]
result=[]
for i in list1:
    if i not in result:
        result.append(i)
print(result)

#sorted list
list1.sort()
print(list1)




    


