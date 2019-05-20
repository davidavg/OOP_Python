'''
Created on Aug 6, 2018

@author: david avalos
'''

#Class declaration
class Person:
    
    algo = "e"
    
    #Constructor declaration
    def __init__(self, **name):
        self.name = name
        print("Person", self.name, "created")
        
    #Method declaration
    def talk(self, words):
        print(words, self.algo)
 
'''
Main Program
'''
        
#Create object
david = Person(y="David",x="Pedro")

#Method call
david.talk("Hello World!")
print(david.algo)