# any error it will not show error 
# get() -> 

dict = {
    1:"one",
    2:"two",
    3:"three",
    (1,2,3):(1,2,3)
}

print(dict.get(2))
print(dict[1]) # same as get 

# POP 

user = {
    'username' : "khushbu",
    "Password" : "*****",
    "Location" : "IN"
}
print(user)
print(user.pop('Location'))

print(user.pop('username' ,'Password'))  # only first pass will be remove 

print(user.pop('Password')) 
print(user)


# popitem ;- return as key pair in tuple , returned lifo
user1 = {
    'username' : "khushbu",
    "Password" : "*****",
    "Location" : "IN"
}

print(user1.popitem())
print(user1.popitem())
print(user1.popitem())
# print(user1.popitem()) # give key error



# modification
user3 = {
    'username' : "khushbu",
    "Password" : "*****",
    "Location" : "IN"
}
print(user3)

user3["Password"] = "***"
print(user3)

# update() - we should pass  in dictionary 
user3.update({'Password' : '1234' , 'is_logged_in': True})
print(user3)

#keys

print(user3.keys())

#values

print(user3.values())

# items 

print(user3.items())