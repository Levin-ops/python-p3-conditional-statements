#!/usr/bin/env python3

def admin_login(username, password):
    if username == "admin" and password=="12345":
        return("Access granted")
    elif username =="ADMIN" and password == "12345":
        return("Access granted")
    elif username !="admin" and password !="12345":
        return ("Access denied")
    else:
        return("Access denied")
    

def hows_the_weather(temperature):
    # your code here
    pass

def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass


# dog = "hungry"

# dict_map ={
#     "hungry":"Refilling food bowl",
#     "thirsty":"refilling water bowl",
#     "playful":"Play tu-of-war",
#     "cuddly":"Snuggling",
# }

# owner = dict_map.get(dog, "Reading newspaper")

# print(owner)