# product filter system
'''Create a JSON file that stores 3 products, each having:
product_name
price
quantity
Then write a Python program to:
Read the JSON file
Print only the products whose price is greater than 500'''

import json
with open("json/products.json","r") as file:
    data=json.load(file)
print(type(data))
print(data)
for product in data["products"]:
    if product["price"]>500:
        print(product)
