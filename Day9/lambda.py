'''
lambda(Anonymous Function):
      1. Lamda is a keyword . which is used to creatte anonymous functions.
      2 . for calling the lambda function , we can store the address  of  lambda 
      inside a variable . by invokking the var_name , we can call the function
'''

## lambda args : <exp>

# result = lambda a,b : a+b ##returns value 
# print(result)
# print(result(1,2))

# (lambda a , b : print(a+b))(int(input("first num : ")),(int(input("second num :"))))


# wap to find square of the number if it is even 

# num = int(input("enter a number"))
# if num % 2==0:
#     print(num**2)
    
# result = lambda num : print(num ** 2) if num %2 == 0 else None    
# result(4)

# lambda args : <exp_1> id <cond> else <exp_2>
## wap to find the square of number if it's even otherwise print cuse of it 

result = lambda num : print(num ** 2) if num%2 == 0 else  print(num **3)
result(3)
result(4)


## positive negative or zero 

result1 = lambda num : print("Positive Number") if num > 0 else  print("Negative") if num < 0 else print("zero") 
result1(1)
result1(0)
result1(-1)