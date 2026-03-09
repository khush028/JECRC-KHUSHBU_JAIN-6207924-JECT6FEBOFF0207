# function in list 
# always modify the perverse object(memory allocation)

# append 

l1 = ["Mango" , "Banana" , "Strawberry"]
print(l1.append("chiku"))
print(l1)

# insert
print(l1.insert(1,"appricot"))
print(l1)

#pop 
print(l1.pop())
# print(l1.pop(5)) index error

##remove  -> it will always remoc=ve first occurenece 

print(l1.remove("Mango"))
print(l1)

#extend
l1.extend(["Apple" ,"Banaa"])
print(l1)
l2=l1.extend("Watermelon")
print(l2)
print(l2)


# Sort help(list.sort)  asecendind oreder , return none beacuse it will not return updated value  reverse = false

l = [23 , 98 ,1 , 97]
l.sort()
print(l) # reverse is false -> ascending

l.sort(reverse=True)
print(l)  # reverse is true -> descending 


#reverse -> only reverse the order not do sorting 

l =[9 ,8,7,6,5,4,3,2,1]
print(l.reverse())
print(l)

l1 = [1,2,3,5,1]
print(l1.reverse())
print(l1)


# index = 

print(l1.index(2))

# count = how many times is occure 

l4 = [1,2,3,1,3,1]
print(l4.count(1))

# clear = remove all items from the list 

l4.clear()
print(l4)