'''
Created on Aug 6, 2018

@author: david avalos
'''

#Class creation
class Employee:
   
    #Constructor declaration 
    def __init__(self):
        print("Employee created")
        
    def work(self):
        print("General employee work")
   
#Class creation    
class HR(Employee):    
    
    def __init__(self):
        print("HR Employee created")
        
    def work(self):
        #Employee.work(self)
        super().work()
        print("Specific HR work")
        
class Engineer(Employee):
    
    def __init__(self):
        print("I'm an engineer!")
        
class Dev(Engineer):
    
    def __init__(self):
        print("I can write code")
        super().__init__()

class Tester(Engineer):
    
    def __init__(self):
        print("I can test code")
        super().__init__()
        
class Automation(Dev, Tester):
    
    def __init__(self):
        #Dev.__init__(self)
        #Tester.__init__(self)
        super().__init__()

'''
Main program
'''
        
print("Objects creation:")  
#hr = HR()            
testeloper = Automation()


print("\nHR's Methods calls:")

#hr.work()