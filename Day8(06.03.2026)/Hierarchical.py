# it is a type oof inhertiance in which the properties will be derived from single parent class to multiple child class


class Parent :
    gold = '2kg'
    silver = '10 kg'
    no_of_flats = 12
    
class SmallestBrother(Parent):
    name = 'Harsh'
    
class ElderBrother(Parent):
    my_name = 'Kartik'

class Sister(Parent):
    sis_name = 'Bhavya'
    
print(SmallestBrother.gold , ElderBrother.silver , Sister.no_of_flats)                
    