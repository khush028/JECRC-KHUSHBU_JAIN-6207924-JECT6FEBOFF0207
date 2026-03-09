def add_nums(*args):
    print(args , type(args))
    sum = 0 
    for i in args :
        sum += i 
    print(f'Adiition : {sum}')
add_nums()        
add_nums(1,2,3,4,5)

# explicit type casting 

def add_nums(*args):
    args = list(args)
    print(args , type(args))
    sum = 0 
    for i in args :
        sum += i 
    print(f'Adiition : {sum}')
add_nums()        
add_nums(1,2,3,4,5)


# printing only float and int values 

def add_nums(*args):
    
    print(args , type(args))
    sum = 0 
    for i in args :
        # if type(i) == int or type(i) == float :
        # if  isinstance( i ,(int , float)):
        if type(i) in (int , float) :
            sum += i 
    print(f'Adiition : {sum}')
add_nums()    
# add_nums(1,2,3,4,5 , 'Hello' , 'khushbu' , '#')

# user input 

add_nums(*eval(input("Enter your list")))


# double packing : - dictionary 

def print_dict(**kwargs):
    print(kwargs)
    
print_dict(username = "1234" , passwor='*****' )    



# prime number , pass n number of input , check prime 

def isPrime(num):
    if num < 2 :
        return False 
    else :
        for i in range (2, num) :
            if num % i == 0 :
                return False
        return True     
                

def find_prime_nums(*args):
    prime = []
     
    for a in args:
        if isPrime(a) :
            prime.append(a)
    return prime    
            

print(find_prime_nums(*eval(input('Enter a nums of list')))) 