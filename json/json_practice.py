import json

# creating a python dictionary and converting it into a JSON string
student = {
    "name":"student1",
      "rollno": 1,
      "ispassedexam":True,
      "score":"80%"
}
data=json.dumps(student)  # convet to JSON string
print(data)


#converting JSON string to python
x= '''{
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "city": "Hyderabad"
}'''
y=json.loads(x)
print(y["email"])

#program to pretty print a JSON object with proper indentation
x= [{
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "city": "Hyderabad"
},
{"name": "lee",
  "email": "lee@gmail.com",
  "city": "Chennai"
},
{"name": "sam",
  "email": "saml@gmail.com",
  "city": "Banglore"},
{"name": "Kiara",
  "email": "Kiaara@gmail.com",
  "city": "Delhi"
  }]
y=json.dumps(x,indent=2)
print(y)

# python list of 5 numbers into JSON format
list=[10,20,30,40,50]
array=json.dumps(list)
print(type(list))
print(array)
print(type(array))

#Parse a JSON string and check whether a key "phone" exists or not.
a= '''{
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "city": "Hyderabad"
}'''
f=json.loads(a)
print(type(f))
if "phone" in f:
    print("yes")
else:
    print("no")