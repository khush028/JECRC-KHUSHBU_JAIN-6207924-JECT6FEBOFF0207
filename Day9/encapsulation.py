# '''
# Encapsulation -> data security 
#                  it is very imp pillar 
#                  it is used to provide security to tha dta (data means variables / prop & methods present inside classs)
                 
#                  THREE ACCESS SPECIFIER 
                 
#                  1 . PUBLIC :- BY DEAFULT 
#                  2 . PEOTECTED (soft barrier ) : -  _a single underscore can be break by any one 
#                  3 . PRIVATE 
                 
# Access Specifier : - it describe who can access the class member (properties &method)  

               
# '''

# ## EXAMPLE FOR PUBLIC ACCESS SPECIFIER 

# class Temp :
#     a , b, *c , d = 'HELLO' #packing
    
#     def greeting(self):
#         print("Hello sir")
        
# class C2(Temp):
#     pass         
        

# # Protected Access Specifier 

# class Temp1:
#     _a = 'khushbu'
#     _b = 10
#     __a = 10 
#     __b = 'I love Python'    
    
# obj= Temp1()
# print(obj._a)
# print(obj._b)
# # print(obj.__a)   


# private 

class Temp :
    __a = 100 
    
    def __status(self):
        print('Class Name is Temp !')
        
    def get(self):
        print(self.__a)
        
    def set(self,new_val):
        self.__a = new_val        
        

obj = Temp()
obj.get()
obj.set(1)
obj.get()
print(obj._Temp__a)


# print(obj.__a)        
# obj.__status()
        

'''
how to access private??

1 . by using syntax 
2 . get & set method
3 . by using @property decorater(setter)
'''
#By using syntax

'''
obj_Name / Class_ name._CN_prop_name/_method_name(accessing)
obj_name/class_name._CN_MemberName = NewValue(Modifing)
'''

# print(obj._Temp__a)
# print(Temp._Temp__a)
# obj._Temp__status()

# def new_method():
#     print('modification')
# obj._Temp__a = '0123456789'  
# obj._Temp__status = new_method
# print(obj._Temp__a)
# obj._Temp__status()  


# # def new_method(self):
# #     Temp._Temp__a = '0123456789'


# by using @property decorator 

class Temp:
    __a = 10 
    
    @property
    def getter(self):
        print(self.__a)
        
    @getter.setter
    def set(self , new_val):
        self.__a = new_val
        
obj = Temp()
obj.getter
obj.set = 1000
obj.getter
print(obj._Temp__a)            