'''

Abstraction : - hiding the internal implementation and showing only functionality to the end user.

Abstract Method :- if a method / function consists of onle declaration not definition not definition then it will be called as "Abstract Method"


Abstract class :-> If a class consists of a atleast one abstract method 

concret class :-> no Abstract method inside the class 

abc : Module
ABC : Abstact  Base Class 



'''
from abc import ABC,abstractmethod
class ATM(ABC):           # we can't create object of ATM     #abstract class
    @abstractmethod
    def generate_pin(self):
        pass
    
    @ abstractmethod
    def forget_pin(self):
        pass 
    
    @abstractmethod
    def check_balance(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass
    
    @abstractmethod
    def deposit(self):
        pass
    
class SBI_ATM(ATM):  # concert class
    def generate_pin(self):
        print("It is used to generate ATM pin")
        
    def forget_pin(self):
        print("It is used to remenber the pin ! if ou forget")
        
    def check_balance(self):
        print("It will the check the balance")
        
    def deposit(self):
        print("Save for international trips") 
        
    def withdraw(self):
        print("do not withdraw the money ! Please")
obj = SBI_ATM()
obj.generate_pin()
obj.check_balance()
obj.forget_pin()
obj.deposit()
obj.withdraw()
        
                       