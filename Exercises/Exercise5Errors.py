'''
Created on Aug 16, 2018

@author: david avalos
'''

class Calculator
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def addition(self):
        return print("\nThe addition of",self.a,"+",self.b,"equals", self.a+self.b,"\n")
    
    def subtraction(self):
        return print("\nThe addition of",self.a,"-",self.b,"equals", self.a+self.b,"\n")
    
    def division(self):
        return print("\nThe addition of",self.a,"/",self.b,"equals", self.a/self.b,"\n")
    
    def multiplication(self):
        return print("\nThe addition of",self.a,"*",self.b,"equals", self.a*self.b,"\n")
    
    def control(self,option):
        
        if option == 1:
            Calculator.addition(self)
        elif option == 2:
            Calculator.subtraction(self)
        elif option == 3:
            Calculator.division(self)
        elif option == 4:
            multiplication(self)
    
while True:
    
    print("*********************\n*****Calculator******","\n*********************")
    selectedOption = int(input("\nPlease choose an option:\n1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n5.Exit\n-->"))
    
    if selectedOptio == 5:
        break
    elif selectedOption <= 0 or selectedOption > 6:
        print("\nThe option you selected is not valid, please try again.\n")
        continue
    
    a = int(input("\nEnter a number 'a' --> "))
    b = int(input("\nEnter a number 'b' --> "))
    
    calculator = Calculator(a)
    calculator.control(selectedOption)
    
print("\nProgram has ended correctly")
    
    