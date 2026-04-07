import json
x= '''[{
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
  }]'''
y=json.loads(x)
print(y)