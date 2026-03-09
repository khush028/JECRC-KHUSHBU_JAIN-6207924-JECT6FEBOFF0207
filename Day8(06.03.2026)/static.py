class Car :
    #Below variables are properties/members/ states 
    wheeler = 4 
    engine = "Petrol"
    base_speed = '40 kmph'
    max_speed = '120 kmph'
    gear = 4 
    
    # TATA = Car()
    # TATA.engine = ['Petrol' , 'Diesel' , 'EV']
    # TATA.air_bags = True
    # TATA.no_of_air_bags = 4 
    # TATA.base_budget = '2l'
    # TATA.no_of_varient = 12 
    
    def __init__(self,air_bags , security , base_budget , varient , total_sale):
        
        self.air_bags = air_bags
        self.security = security
        self.base_budget = base_budget
        self.varient = varient
        self.total_sale = total_sale
        
        # functionaity object 
    def display_properties(self):
        print({
            'Wheelers' : self.wheeler,
            'engine' : self.engine,
            'base_speed' : self.base_speed,
            'max_speed' : self.max_speed
            
        })   
        
        
    @classmethod
    def update_gears(cls,new_gears):
        cls.gear = new_gears
        print(f'update gears : {cls.gear}')
            
        
    def update_base_speed(self , new_speed):
        self.base_speed = new_speed
        print(f" New base_spedd : {self.base_speed}") 
        
    @staticmethod
    def greeting(name):
        print(f'GOOD MORNING:{name}')        
        
TATA = Car(True , 'Level 5' , '2L' ,12 ,100000)
print("properties before updation")
print(TATA.display_properties())
print("properties after updation ")
TATA.update_base_speed("60kmph")
TATA.update_gears(5)
           
# to remove number lines of code resuability we use constructor   
# constructor (__init__)

#Syntax

'''
class ClassName:
      properties
      
      def __init__(self , arg1 , arg2 , arg3, ... ,argn):
      self.arg1 = arg1
      self.arg2 = arg2   standard method to use args give sign that it'sconstructor and it will add memory
      .
      .
      .
      self.argn = argn
'''
    
    
    