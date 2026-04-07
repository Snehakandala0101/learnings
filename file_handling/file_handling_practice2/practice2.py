#student marks system
with open("marks.txt","a") as f:
    name=input("enter name: ")
    marks=input("enter marks: ")
    f.write(f"{name}-{marks}\n")
print("student record saved successfully")
