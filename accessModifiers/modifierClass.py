'''
Created on Sep 19, 2018

@author: david avalos
'''

from Examples import AccessModifiers

class classC:


    def __init__(self):
        self.objA = AccessModifiers.classA("public","protected","private")
    
    def printVariablesC(self):
        print(self.objA.public)
        print(self.objA._protected)
        print(self.objA.__private)
        
'''
Main
'''

C = classC()

C.printVariablesC()
    