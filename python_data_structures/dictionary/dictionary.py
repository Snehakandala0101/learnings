#check whether a key exists or not
d={"name":"x1","age":20,"studying":"yes"}
print("age" in d.keys())

#count frequency of each character using dictionary
a="hello people"
d1={}
for ch in a:
    if ch in d1:
        d1[ch]+=1
    else:
        d1[ch]=1
print(d1)

#count frequency od each word in a sentence
sentence="Never give in ,never give in,never,never,never"
words=sentence.split()
d2={}
for word in words:
    if word in d2:
        d2[word]+=1
    else:
        d2[word]=1
print(d2)

#finding the key with maximum value in a dictionary
d3={"a":22,"b":66,"c":102}
print(max(d3))

d4={"a":1,"b":2}
d5={"b":3,"c":4}
d4.update(d5)
print(d4)

#swap keys and values
swapped={}
for key,values in d3.items():
    swapped[values]=key
print(swapped)


#convert two lists into dictionary
keys=["name","age","city"]
values=["alyzha",15,"chennai"]
result={}
for i in range(len(keys)):
    result[keys[i]]=values[i]
print(result)