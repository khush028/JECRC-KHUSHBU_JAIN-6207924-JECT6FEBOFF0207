class Temp:
    
    def sum(self,a,b):
        print(a+b)
    ##  Monkey Patching :- is a process of storing the pre method's address inside a variable 
    ## before overring the method area's address . using the var , we can acess it     
    add_sum = sum
    def sum (self ,a,b,c):
        print(a+b+c)
        
obj = Temp()
# obj.sum(10,90)   #  python will not execute this it will always take new method 
obj.add_sum(10,90)
obj.sum(10,20,30)
        