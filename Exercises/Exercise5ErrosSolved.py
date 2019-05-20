'''
Created on Aug 16, 2018

@author: david avalos
'''

class Calculator:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def addition(self):
        return print("\nThe addition of",self.a,"+",self.b,"equals", self.a+self.b,"\n")
    
    def subtraction(self):
        return print("\nThe addition of",self.a,"-",self.b,"equals", self.a-self.b,"\n")
    
    def division(self):
        return print("\nThe addition of",self.a,"/",self.b,"equals", self.a/self.b,"\n")
    
    def multiplication(self):
        return print("\nThe addition of",self.a,"*",self.b,"equals", self.a*self.b,"\n")
    
    def control(self,option):
        
        try:
            if option == 1:
                Calculator.addition(self)
            elif option == 2:
                Calculator.subtraction(self)
            elif option == 3:
                Calculator.division(self)
            elif option == 4:
                Calculator.multiplication(self)
        except:
            print("\noops! something went wrong try again :)\n")
    
while True:
    
    print("*********************\n*****Calculator******","\n*********************")
    try:
        selectedOption = int(input("\nPlease choose an option:\n1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n5.Exit\n-->"))
    except ValueError:
        print("\nSorry, non-numeric entries are not allowed. Please, try again.\n")
        continue
        
    if selectedOption == 5:
        break
    elif selectedOption <= 0 or selectedOption >= 6:
        print("\nThe option you selected is not valid, please try again.\n")
        continue
    
    try:
        a = int(input("\nEnter a number 'a' --> "))
        b = int(input("\nEnter a number 'b' --> "))
    except ValueError:
        print("\nSorry, non-numeric entries are not allowed. Please, try again.\n")
        continue
    
    calculator = Calculator(a, b)
    calculator.control(selectedOption)
    
print("\nProgram has ended correctly")
    
    