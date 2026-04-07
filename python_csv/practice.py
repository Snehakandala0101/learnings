import csv
#reading csv file
with open("python_csv/students.csv","r",newline="") as csv_file:
    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        print(line)

#counting records
count=0
with open("python_csv/students.csv","r",newline="") as csv_file:
    csv_reader=csv.reader(csv_file)
    next(csv_reader)   #skips header
    for line in csv_reader:
            count+=1
    print(count)

#counting no of students who scpred greater thn 80
count=0
with open("python_csv/students.csv","r",newline="") as csv_file:
    csv_reader=csv.reader(csv_file)
    next(csv_reader)   #skips header
    for line in csv_reader:
            if int(line[2])>80:
                  count+=1
    print(count)

#find highest and lowest marks students
with open("python_csv/students.csv","r",newline="") as csv_file:
    csv_reader=csv.reader(csv_file)
    next(csv_reader)   #skips header

    highest_marks=0
    highest_student=""

    lowest_marks=0
    lowest_student=""
    for line in csv_reader:
        name=line[0]
        marks=int(line[2])

        if marks>highest_marks:
            highest_marks=marks
            highest_student=name
        if marks<highest_marks:
            lowest_marks=marks
            lowest_student=name
print("Highest:",highest_student,highest_marks)
print("Lowest:",lowest_student,lowest_marks)

#searching for a student
found=False
with open("python_csv/students.csv","r",newline="") as csv_file:
    csv_reader=csv.reader(csv_file)
    next(csv_reader) 
    user=input("enter a student name")
    for line in csv_reader:
        if line[0]==user:
            print("Found",line)
            found=True
            break
if not found:
    print("Not Found")
        
