# Multilevel -> it is a type of inheritance in which the properties will be deriverd frome ont to another class by consedering more than one level

#syntax : all the properties are drie in sequential 

class Class1:   # parent
    a = "class_1"
class Class2(Class1): # child
    b = 'class_2'
class Class3(Class2):
    c= 'class_3'
class Class4(Class3):
    d = 'class_4'
class Class5(Class4):
    e = 'class_5'    
    
obj = Class5()
print(obj.a,obj.b,obj.c,obj.d,obj.e)