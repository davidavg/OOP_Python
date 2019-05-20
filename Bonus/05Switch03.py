'''
Created on Oct 3, 2018

@author: david avalos
'''
#Declare functions
def sum():
    print("\nExecute a sum")
    
def subtraction():
    print("\nExecute a subtraction")
        
def multiplication():
    print("\nExecute a multiplication")
    
def division():
    print("\nExecute a division")

#Create a dictionary with the different options
MyDic = {
    "SUM": sum,
    "SUBTRACTION": subtraction,
    "MULTIPLY": multiplication,
    "DIVIDE": division
    }

#Ask for user input
userInput = input("Please introduce one option:\nSum\nSubtraction\nMultiply\nDivide\n-->").upper()

#Save the function name
#functionToCall = MyDic[userInput]

#Execute the function
#functionToCall()

#Execute the function without saving function name first
MyDic[userInput]()
