'''
Created on Oct 3, 2018

@author: david avalos
'''
#Create a dictionary with the different options
MyDic = {
    "SUM": "\nExecute a sum",
    "SUBTRACTION": "\nExecute a subtraction",
    "MULTIPLY": "\nExecute a multiplication",
    "DIVIDE": "\nExecute a division"
    }

userInput = input("Please introduce one option:\nSum\nSubtraction\nMultiply\nDivide\n-->").upper()

print(MyDic[userInput])