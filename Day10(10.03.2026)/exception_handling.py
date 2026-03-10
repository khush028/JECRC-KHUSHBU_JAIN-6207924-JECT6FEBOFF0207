#Exception :- Unauthorized Event , Flow of the execution of the program will be stopped 
#after that it will never execute the further code 
# syntax error 
'''
try : - we will put the problem statment (block of code due to which we might get error)
****except : - we put actual solution for the errror  .
                solution :-  Resolution for error from code
                Due to execpt block we can prevent the  unauthorized events (errors)
                If the color is purple or pink iT's mean execption (class)
                Red  :- error (object)
                Purple : - Warning (old approach)
                
finally : - After getting error or after resolution , force fully if we want to execute any particular block of code , then we use finally block .

else : - IT'S an alternative of try block , if we find out any error inside try block interpreter will move fwd twd else block , if code correct it wil give ouput , if code incorrect it will give error

output :- error - 1. error name
                  2. reason
                  3. line no 
                  
      HOW TO HANDLE EXECPTION ?
      
      --> sPECIFIC Execption Handling  : -  if we are ever of the error or exception then we can go with specififc 
      try : 
           problem 
           statment
           
      except ErrorName:
            resolution
            solution code 
                 
      --> Generic Exception Handling
      --> Default Exception Handling
      
      
                  
'''
'''
 --> sPECIFIC Execption Handling  : -  if we are ever of the error or exception then we can go with specififc 
      try : 
           problem 
           statment
           
      except ErrorName:
            resolution
            solution code 
'''


n1 ,n2 = 10 , 0
# print(n1/n2)
try:
# # problem satement
     result = n1/n2
     print(result)
except ZeroDivisionError :
     # resolution statement
    print('Please do not choice zero as the second number')
    
    
# print("codee after try execpt - 01")
# print("codee after try execpt - 02")
# print("codee after try execpt - 03")


# handle error of  mvc

# try:
#     a,b,c = 1,2  #no such memoery wil be store 
# except ValueError:
#     print("FOR PERFORMING MVC , no of variable should be equals to no of values!")    
# try :
#     print(a,b,c)
    
# except NameError:
#     print("Identifiers not in the memory")
    
    
    
# import time  
# try: 
#     while  True:
#         print(time.time())
# except KeyboardInterrupt:
#     print("loop got stopped")      
        
    
    
'''
generic : - Manual work reduce , no need to remember the error name
            IT is type of execption handling in which no need to pass any  particular execption class name . Instead of we can use parent "Exception " class Called 'Execption'
            
--- using "genric execption handling " , we can't handle keyboard interuption /(infinite loop)
'''

# try:
#     a,b,c = 1,2  #no such memoery wil be store 
# except Exception:
#     print("FOR PERFORMING MVC , no of variable should be equals to no of values!")    
# try :
#     print(a,b,c)
    
# except Exception:
#     print("Identifiers not in the memory")
    
# import time  
# try: 
#     while  True:
#         print(time.time())
# except Exception:
#     print("loop got stopped")    



# default : -  It is type of execution handling in which we can handle all types of errors or execption execpt "Syntax Error"

     
import time  
try: 
    while  True:
        print(time.time())
except :
    print("loop got stopped")      
           
  
    
    