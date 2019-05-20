'''
Created on Oct 3, 2018

@author: david avalos
'''

#Ask for user input
option = input("Please introduce one option:\nSum\nSubtraction\nMultiply\nDivide\n-->")

#Switch
if option == "Sum":
    print("\nExecute a sum")
elif option == "Subtraction":
    print("\nExecute a subtraction")
elif option == "Multiply":
    print("\nExecute a multiplication")
elif option == "Divide":
    print("\nExecute a division")
else:
    print("\nInvalid option")    