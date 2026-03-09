# function for string data types 

s = "PythON"
print(s.lower()) # return value

result = s.upper()
print(result)

s1 = "python"
print(s1.capitalize())

# title 
s2 = "khushbu is a good girl"
print(s2.title())

#strip    only starting and ending space or character 
s3 = "   khushbu is   "
print(s3.strip())

#lstrip    remove only left side whitespaces and charcter will remove 
print(s3.lstrip())

#rstrip    remove  spaces and charcter from right side 

print(s3.rstrip())

# replace 

s4 = "khushbu is a coder "
print(s4.replace('coder' , 'dancer'))
print(s4.replace('k','K'))  # we can also update the single character in it 

#index  = if index not present it will give output as valueerror 

fruits = ["apple", "banana", "mango", "orange"]
print(fruits.index("mango"))
# print(fruits.index("mang0"))

# find = if find not able to find then it will give -1

fruits1 = "Mango"
print(fruits1.find("M"))
print(fruits1.find("0"))


# split() -> string to list (separate all value)  compiler

s6 = "MY NAME IS KHUSHBU"
print(s6.split())
print(s6.split('KHUSHBU'))
print(s6.split('-'))

#join() -> only in compiler

l1 = ["khushbu" ,"is" , "good" ]

''.join(l1)

# startswith

l2 = 'khushbu'
print(l2.startswith('s'))
print(l2.endswith('u'))
print(l2.isdigit())
print(l2.isalpha())
print(l2.islower())
print(l2.isupper())






