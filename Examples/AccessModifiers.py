'''
Created on Aug 6, 2018

@author: david avalos
'''
from Examples import SuperKeyWord
from accessModifiers import modifierClass

#Class declaration
class classA:
    
    def __init__(self, public, protected, private):
        #Variables with different access modifiers created at class level
        self.public =  public
        self._protected = protected
        self.__private = private
        x = modifierClass.classC()
        
    def test(self):
        print("Test")
        
    def printVariables(self):
        print(self.public)
        print(self._protected)
        print(self.__private)
        
        
class subClassA(classA):
    
    def printVariables(self):
        print(self.public)
        print(self._protected)
        #print(self.__private)
        
class classB:
    
    def getPublicVariable(self):
        A = classA("Public", "Protected", "Private")
        print("Public variable from class A:",A.public)
        
    def getProtectedVariable(self):
        A = classA("Public", "Protected", "Private")
        print("Protected variable from class A:",A._protected)

    def getPrivateVariable(self):
        A = classA("Public", "Protected", "Private")
        print("Private variable from class A:",A.__private)
        
    def accesMethodTest(self):
        A = classA("Public", "Protected", "Private")
        A.test()

'''
Main program
'''
'''
#Create class A object 
A = classA("Public", "Protected", "Private")

print("Print variables from Class A on Main program:\n")

#Access variables from class A on main program
print("This is a", A.public, "variable from main program")
print("This is a", A._protected, "variable from main program")
#print("This is a", A.__private, "variable from main program")
A.printVariables()

#A.test()

  
#Create sub-class A object
subA = subClassA("Public", "Protected", "Private")

print("\nSub-Class A:\n")

#get variables from class A on sub-class
subA.printVariables()

#subA.test()

print("\nClass B:\n")

#Create class B object
B = classB()

#get variables from class A on class B
B.getPublicVariable()
B.getProtectedVariable()
#B.getPrivateVariable()
#B.accesMethodTest()
'''
