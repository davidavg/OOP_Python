'''
Created on Oct 2, 2018

@author: david avalos
'''

#Create class
class Calculator:
    
    def sum(self):
        print("\nExecute a sum")
        
    def subtraction(self):
        print("\nExecute a subtraction")
            
    def multiplication(self):
        print("\nExecute a multiplication")
        
    def division(self):
        print("\nExecute a division")
        
'''
Main
'''

#Create object from Calculator class
myCalculator = Calculator()

#Create dictionary with methods as values. This will simulate a switch
MyDictionary = {
        "SUM": myCalculator.sum,
        "SUBTRACTION": myCalculator.subtraction,
        "MULTIPLY": myCalculator.multiplication,
        "DIVIDE": myCalculator.division,
    }

#Ask for user input
userInput = input("Please introduce one option:\nSum\nSubtraction\nMultiply\nDivide\n-->").upper()

#We call the method the user selected
MyDictionary[userInput]()