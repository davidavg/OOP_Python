'''
Created on Aug 13, 2018

@author: david avalos
'''

class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def addition(self):
        print(self.a+self.b)
        
    def subtraction(self):
        print(self.a-self.b)
        
obj = Calculator(5,2)
obj.addition()
obj.subtraction()
        
        
    