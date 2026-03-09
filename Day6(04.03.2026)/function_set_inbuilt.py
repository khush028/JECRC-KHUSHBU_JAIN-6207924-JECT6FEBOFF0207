# add() -> 1 argument should be pass that argument should not prensent in set already because set only conatin unique element  also no changes will be show 

s = {1 ,2 ,4 , True , False , 0 , 3+9j}
print(s) # nearset pointer and fetch the value 

s.add(4)
# we can't set = {1,2,3,{2}} only mutable data type we can add tuple in nested 

print(s) # it's will add the value but it's remove automatically by the set 

s.add(('khushbu' , 'Jain'))
print(s)

# remove ;- removing element should be member of its , else keyerror 

print(s.remove(3+9j))
print(s)

print(s.remove(True))
print(s)

# print(s.remove(10))     # key error 
# print(s)


# discard ;- same as remove but not show error it wil show missing element 

print(s.discard(10)) # it will not show error show none 

print(s.pop()) # randomly remove 
print(s)

# deafult value of set is set()
#set() - is a sobject beacuse call as a class 

# clear -> only empty set will remain 

print(s.clear())
print(s)



# union;- return a new set with elements from the set and all others  

s1 = {1,2,3}
print(s1)
s2 ={2,3,4}
print(s2)
s3 = s1.union(s2) # we can pass multiple arguments by using , (comas)
print(s3)
print(s1.union({1,2,3} , {3,5,6} ,{9,5,6}))

# sintersecttion - comman 

print(s1.intersection(s2))

# difference ;- not comman 
print(s1.difference(s2))
print(s2.difference(s1))

# symmetric difference ;- not comman elements in both 
print(s1.symmetric_difference(s2))
