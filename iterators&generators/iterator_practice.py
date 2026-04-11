#manual iteration

list_data=[2,4,6,8,10]
it=iter(list)

while True:
    try:
        value=next(it)
        print(value)
    except  StopIteration:
        break


#check iterable vs iterator
my_list=["He","is","a","Monster"]
#check list
print("Is list an iterator?",hasattr(my_list,"__next__"))
#convert to iterator
it=iter(my_list)
#check iterator
print("Is iterator an iterator?",hasattr(it,"__next__"))


#loop internals
tuple_data=(3,6,9,12,15,18,21)
it=iter(tuple)

while True:
    try:
        value=next(it)
        print(value)
    except  StopIteration:
        break


#custom range iterator
class My_range:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.current=start

    def __iter__(self):
        return self
    def __next__(self):
        if self.current<self.end:
            value=self.current
            self.current+=1
            return value
        else:
            raise StopIteration
for num in My_range(1,10):
    print(num)


#even Number iterator
class Even_numbers:
    def __init__(self,max):
        self.max=max
    def __iter__(self):
        self.current=2
        return self
    def __next__(self):
        if self.current<=self.max:
            value=self.current
            self.current+=2
            return value
        else:
            raise StopIteration
for num in Even_numbers(20):
    print(num)



#reverse string iterator
class ReverseString:
    def __init__(self,text):
        self.text=text
    def __iter__(self):
        self.index = len(self.text) - 1
        return self
    def __next__(self):
        if self.index >= 0:
            value = self.text[self.index]
            self.index -= 1
            return value
        else:
            raise StopIteration

for ch in ReverseString("hello"):
    print(ch)