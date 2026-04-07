# add a new product in products.json


import json
with open("json/products.json","r") as file:
    data=json.load(file)

#take new input
product_name=input("enter a new product")
price=float(input("enter price"))
quantity=int(input("enter quantity"))

#create new product directory
new_product={
    "product_name":product_name,
    "price":price,
    "quantity":quantity
}

#append new product to list
data["products"].append(new_product)

#write updated data back to file
with open("json/products.json","w") as file:
    json.dump(data,file,indent=4)
print("product added successfully!")
