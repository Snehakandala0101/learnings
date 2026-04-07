import csv

#add new record
name=input("enter name")
rollno=input("enter his/her rollno")
marks=input("enter his/her marks")
with open("python_csv/students.csv","a",newline="") as csvfile:
    csv_append=csv.writer(csvfile)
    rows=[name,rollno,marks]
    csv_append.writerow(rows)
    print("updated success")

#update student marks
name=input("enter name")
update_marks=input("enter his/her marks")
rows=[]
found=False
with open("python_csv/students.csv","r") as csvfile:
    csvread=csv.reader(csvfile)
    for row in csvread:
        if row[0]==name:
            row[2]=update_marks
            found=True
        rows.append(row)
if found:
    with open("python_csv/students.csv","w",newline="") as csvfile:
        csvappend=csv.writer(csvfile)
        csvappend.writerows(rows)
    print("Marks updated successfully")
else:
    print("Student not found.No changes made.")

#delete student record
name=input("enter name")
rows=[]
found=False
with open("python_csv/students.csv","r") as csvfile:
    csvread=csv.reader(csvfile)
    for row in csvread:
        if row[0]==name:
            found=True
    rows.append(row)
if found:
    with open("python_csv/students.csv","w",newline="") as csvfile:
        csvappend=csv.writer(csvfile)
        csvappend.writerows(rows)
    print("deleted")
else:
    print("Student not found.No changes made.")

#creating result system
updated_rows=[]
with open("python_csv/students.csv","r") as csvfile:
    csvread=csv.reader(csvfile)
    header=next(csvread)
    updated_rows.append(header)
    for row in csvread:
        if int(row[2])>=40:
            result="Pass"
        else:
            result="Fail"
        row.append(result)
        updated_rows.append(row)
with open("python_csv/result.csv","w",newline="") as csvfile:
    csvappend=csv.writer(csvfile)
    csvappend.writerows(updated_rows)
print("Result System created successfully")

