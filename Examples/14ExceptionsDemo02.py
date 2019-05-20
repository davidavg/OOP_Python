'''
Created on Aug 9, 2018

@author: david avalos
'''

'''
General exception
'''

#Execute an instruction
i = input("Enter another number: ")

#try the code to see if it contains an exception
try:
    i = int(i)
except:
    print("Please enter a number next time")
else:
    print(i**2)

'''
Particular exception
'''

#Execute an instruction
i = input("Enter one more number: ")
myList = (0,1)

#try the code to see if it contains an exception
try:
    i = int(i)
    print(myList[5])
except ValueError:
    print("You did not enter a number")
except:
    print("Something else went wrong")
else:
    print(i**2)