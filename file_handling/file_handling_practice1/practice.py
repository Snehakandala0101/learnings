#creating a file and write some text in it
f= open("sample.txt","w") 
f.write("Hello Python \nWelcome to File Handling")
f.close()

#reading the content of the file and printing it
f1=open("sample.txt","r")
print(f1.read())
f1.close()

#reading the content line by line using readline()
with open("sample.txt","r") as f2:
    line1=f2.readline()
    print(line1) 
    line2=f2.readline()
    print(line2)

#reading the content using loop method
with open("sample.txt","r") as f3:
    for line in f3:
        print(line.strip())    # strip() to remove extra spaces

#append data
with open("sample.txt","a") as f4:
    f4.write("\nThis is appended text.")

#read a file and count number of characters and number of words
count=0
with open("sample.txt","r") as f5:
    content=f5.read()
#count characters
char_count=len(content)
#count words
words=content.split()
word_count=len(words)
print("no of characters=",char_count)
print("no of words=",word_count)

#count lines
count=0
with open("sample.txt","r") as f6:
    for line in f6:
        count+=1
    print(count)

    
#return the word if found else not
word=input("enter a word to search")
found= False
with open("sample.txt","r") as f7:
    for line in f7:
        if word in line:
            found=True
            break
if found:
    print("word found")
else:
    print("not found")

#copy content from file text to another text
with open("sample.txt","r") as source:
    with open("copy.txt","w") as destination:
        for line in source:
            destination.write(line)
print("File copied successfully.")

# read file content and write it into a new file in uppercase
with open("sample.txt","r") as file:
    with open("copy.txt","w") as new_file:
        for line in file:
            new_file.write(line.upper())
print("conversion to uppercase is completed")

#reverse file content
with open("sample.txt","r") as file:
    content=file.read()
reversed_content=content[::-1]
with open("reverse.txt","w") as new_file:
    new_file.write(reversed_content)
print("reversing file content is completed")
    
