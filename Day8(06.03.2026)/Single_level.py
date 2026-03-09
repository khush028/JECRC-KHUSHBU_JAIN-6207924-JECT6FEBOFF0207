#INHERITANCE 
''' 
1. single level -> we have only a single parent and single child. also the properties will be derieved only one time.
'''
## super class -> the classs from which we are going to derieve the properties
class Parent:    # parent class # super class
    bank_balance = '54L'
    
    def __init__(self,*member):    # chaining
        self.member = member
        
    def desc(self):
        print('I am the parent class')

# sub -> the class in which we are going to derieve the properties        
class Child(Parent):  ## child class or sub class 
    
    def __init__(self,child_name, *args):    ## chaining
        super().__init__(args)
        self.child_name = child_name
    

## Constructor chaining : calling parents class's constructor from inside child class constructor 

obj = Child('khushbu','MOM','DAD')
print(obj.child_name)
print(obj.member)
print(obj.bank_balance)
obj.desc()        
        