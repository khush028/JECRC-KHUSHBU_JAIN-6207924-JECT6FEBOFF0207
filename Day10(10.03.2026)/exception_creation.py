'''

raise :- I t is a keyword , which helpd us to throw an error in between a program

Exception Creation : - 

1 . custom Exception 
'''

'''
Custom Exception 
 1. we use pre - built Exception classes according to our requirement 
 
 raise ValueError("message ")
 
 ValueError : message 
 
'''

# num = 17 
# # num = 19
# if num >=18 :
#     print("You ARE Eligible for Voting & dRIVING") 
# else :
#     # raise ValueError("Age should be greater than or equal to 18")    
#     raise KeyboardInterrupt("You are under age ")


'''
User - defined Exception 

  1. iT is a type of execption in which we can create our own exception classes based upon our own requriement . we can also provide names to those classes according tht user cases.
'''
# class MyExecption(Exception):
#     pass
# # raise MyExecption("this is my execption")


# n1 , n2 = 10 , 0  

# if n2 == 0 :
#     raise MyExecption("secong num can't be zero")
# else:
#     print(n1/n2)
    
'''

Assertion Exception : - can be created by using one keyword called "assert".

assert<condition> , print(ERROR)
print(output)
'''

s = input("Enter a string")
assert s == s[::-1] , print("It's not a palindrome string")
print("It's a palindrome string")


