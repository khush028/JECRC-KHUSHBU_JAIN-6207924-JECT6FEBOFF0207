'''
---operator overloading :- It is a phenomemon of making the operators to work on user designed data types by invoking respective magic methods.

--Magic Methid -> (DUNDAR) it is special type of method in which double underscore will be there at staring and ending of the method name . 

--Example 
    1. __add__
    2. __sub__
    3. __mul__
    4. __floordiv__
    5. __truediv__
    6. __mod__
    
If we don't use operator overloading then what will happen ?
For using the operators inside user-defined data types we have to use operator overloading .

--Syntax -> 
    class ClassName:
        def __init(self,val):
            self.val = val 
            
        def __add__(self,ano_obj):
             return self.val +ano._obj.val :
             
    obj1 = ClassName(val1)
    obj2 = ClassName(val2)  
    print(obj1+obj2)      ## obj1.__add__(obj2)               
    
'''

class MyDt:
    def __init__(self , val):
        self.val = val 
        
    def __str__(self):
        return str(self.val)
        
        
    def __add__(self,*ano_val):
        sum = self.val
        for i in ano_val:
            sum += i.val
        return MyDt(sum)    
        # return self.val + ano_val.val    
    
    def __sub__(self, *ano_val):
        # return self.val - ano_val.val
        sub = self.val
        for i in ano_val:
            sub -= i.val
        return MyDt(sub)    
    
    # def sub(self, *args):
    #     sub = self.val
    #     for i in args :
    #         sub -= i.val
    #     return sub    
    
    def __mul__(self, *ano_val):
        # return self.val * ano_val.val
        mul = self.val
        for i in ano_val:
            mul *= i.val
        return MyDt(mul)    
    
    # def mul(self,*args):
    #     mul = self.val
    #     for i in args:
    #         mul *= i.val
    #     return mul    
    
    def __floordiv__(self, ano_val):
        return self.val // ano_val.val
    
    def __truediv__(self, ano_val):
        return self.val / ano_val.val
    
    def __mod__(self, ano_val):
        return self.val % ano_val.val
    
    # def __add__(self,*args):
    #     sum = self.val
    #     for i in args :
    #         sum += i.val
    #     return sum    
    
    # def add_nums(self,*args):
    # # print(args , type(args))
    #    sum = self.val 
    #    for i in args :
    #        sum += i.val 
    #    return sum
    
# print("ADDition of multiple = " ,MyDt.add_nums(MyDt(10.10))+MyDt.add_nums(MyDt(10)) + MyDt.add_nums(MyDt(90)))
print("Additio of multiple" , MyDt(10) + MyDt(90) + MyDt(80))
print("Subtraction of multiple values = " , MyDt(10) - MyDt(9) - MyDt(2))
print("Multiple of multiple values =" , MyDt(11) *MyDt(9) * MyDt(1))
# print("subtraction of multiple = " ,MyDt.sub(MyDt(90))-MyDt.sub(MyDt(10)) - MyDt.sub(MyDt(20)))
# print("Multiplication of multiple = " ,MyDt.mul(MyDt(90))*MyDt.mul(MyDt(10))*MyDt.mul(MyDt(20)))
print('Addition =' , MyDt(5) + MyDt(5))
print("Subtraction = " ,MyDt(10)-MyDt(5))    
print("Multiplication = ", MyDt(5)*MyDt(5))
print("Floor division =" ,MyDt(6)//MyDt(3))
print("True division = ",MyDt(6) / MyDt(3))
print("Mod = " ,MyDt(6)% MyDt(3))

        