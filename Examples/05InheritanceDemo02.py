'''
Created on Aug 6, 2018

@author: david avalos
'''

#Class creation
class Employee:
   
    #Constructor declaration 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("Employee", self.name, "created with salaray of",self.salary)
        
    def work(self):
        print("General employee work")
        
    def recRoom(self):
        print("Mario Kart!")
   
#Class creation    
class HR(Employee):    
    
    def work(self):
        print("Specific HR work")
        
    def organizeEvent(self):
        print("Organize event")
        
class Engineer(Employee):
    
    def work(self):
        print("Engineer engineering things on some software or something")
        
    def takeTraining(self):
        print("Taking engineer training")

'''
Main program
'''
        
print("Objects creation:")              
#Objects creation
david = Engineer("David",10000)
hr = HR("Julieta", 9000)

print("\nEngineer's Methods call:")

#Engineer's methods call
david.work()
david.recRoom()
david.takeTraining()

print("\nHR's Methods calls:")

#HR's methods call
hr.work()
hr.recRoom()
hr.organizeEvent()