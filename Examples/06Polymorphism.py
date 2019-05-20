'''
Created on Aug 6, 2018

@author: david avalos
'''

#Class declaration
class classA:

    #Empty constructor
    def __init__(self):
        pass
    
#Class declaration
class classB:
    
    #Empty constructor
    def __init__(self):    
        pass

'''
Main program
'''
   
#Assign first value, an Integer
polymorphism = 123
print("First value:",polymorphism)

#Assign second value, an object
polymorphism = classA()
print("\nSecond value:", polymorphism)

#Assign third value, a string
polymorphism = "Polymorphism rules!"
print("\nThird value:",polymorphism.upper())

#Assign fourth value, another object
polymorphism = classB()
print("\nFourth value:",polymorphism)