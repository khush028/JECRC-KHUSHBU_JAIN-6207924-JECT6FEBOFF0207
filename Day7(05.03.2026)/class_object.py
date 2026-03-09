class Car:    # we can't leave one empty block we can use pass keyword 
    
    # Below variables are properties/members/ states 
    wheeler = 4 
    engine = "Petrol"
    base_speed = '40 kmph'
    max_speed = '120 kmph'
    gear = 4 
    

# Below instances are called as objects     
TATA = Car()

# below properties , we cand add some new properties in oops 

TATA.air_bags = True
TATA.Security = "Level 5"

# For Accessing the properties , we have to follow the below syntax :
print("Properties of TATA")
print(f'No of wheelers : {TATA.wheeler}')
print(f'Engine Type : {TATA.engine}')
print(f'Base Speed : {TATA.base_speed}')
print(f'Max speed  : {TATA.max_speed}')
print(f'No of Manual Gears : {TATA.gear}')
print(f'Air BAgs: {TATA.air_bags}')
print(f'Security : {TATA.Security}')
print()

mahindra = Car()
print("Properties of MAHINDRA")
print(f'No of wheelers : {mahindra.wheeler}')
print(f'Engine Type : {mahindra.engine}')
print(f'Base Speed : {mahindra.base_speed}')
print(f'Max speed  : {mahindra.max_speed}')
print(f'No of Manual Gears : {mahindra.gear}')
print()
suzuki = Car()
print("Properties of SUZUKI")
print(f'No of wheelers : {suzuki.wheeler}')
print(f'Engine Type : {suzuki.engine}')
print(f'Base Speed : {suzuki.base_speed}')
print(f'Max speed  : {suzuki.max_speed}')
print(f'No of Manual Gears : {suzuki.gear}')
print()
toyota = Car()
print("Properties of TOYATA")
print(f'No of wheelers : {toyota.wheeler}')
print(f'Engine Type : {toyota.engine}')
print(f'Base Speed : {toyota.base_speed}')
print(f'Max speed  : {toyota.max_speed}')
print(f'No of Manual Gears : {toyota.gear}')
print()\
    
    # cd day7 
    # py 
    # import class_object 
    

    
    