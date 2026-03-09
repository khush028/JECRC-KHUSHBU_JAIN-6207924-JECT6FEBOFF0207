''' IT is a type of inhertiance in which the properties will be derived from multiple parent class to a single child class'''


class Parent_1:
    a = 10 
class Parent_2:
    b = 34
class Parent_3:
    c = 8  
class Parent_4:
    d = 45      
class Child(Parent_1,Parent_2,Parent_3,Parent_4):
    pass

# obj = Child()
# print(obj.a,obj.b,obj.c,obj.d)      

print(Child.a , Child.b , Child.c ,Child.d)  #because we don't have self that's why we can use it 
    