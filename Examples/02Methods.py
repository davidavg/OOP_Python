'''
Created on Aug 6, 2018

@author: david avalos
'''

#Class declaration
class Person:

    #Constructor declaration
    def __init__(self):
        print("Person created")
    
    #Method declaration
    def talk(self, words):
        print(words)
    
    def walk(self):
        pass  
    
'''
Main program
'''        
        
#Create object
david = Person()

#Method call
david.talk("Hello World!")