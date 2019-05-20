'''
Created on Aug 9, 2018

@author: david avalos
'''

'''
Syntax Error
'''

x = 0

if x%2 == 0:
    print("True condition")
else:
    print("False condition")
    
'''
Logic error
'''    

while x < 10:
    print("I am error",x)
    x+=1
    
'''
Execution Error
'''
i = input("Enter a number: ")
i = int(i)

print(i**2)