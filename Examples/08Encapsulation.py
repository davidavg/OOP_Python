'''
Created on Aug 6, 2018

@author: david avalos
'''

#class declaration
class classA:

    #class constructor
    def __init__(self, encapsulation):
        self.__encapsulation = encapsulation
    
    #getter
    def getEncapsulation(self):
        return self.__encapsulation
    
    #setter
    def setEncapsulation(self, value):
        #
        #
        #
        self.__encapsulation = value
        
'''
Main program
'''
#Crate class a object
A = classA("Encapsulation test!")

#print the current value of the encapsulated variable
print("This is the value of our encapsulated variables:",A.getEncapsulation())

#Change the value of the encapsulated variable
A.setEncapsulation("The new encapsulated value!")

#Print the new value of the encapsulated variable
print("\nThis is the new value of the encapsulated variable:",A.getEncapsulation())
