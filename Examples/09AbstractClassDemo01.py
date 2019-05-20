'''
Created on Aug 6, 2018

@author: david avalos
'''

#import abstract library
from abc import abstractmethod, ABC

#Class declaration
class Employee(ABC):
    
    #Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("Employee", self.name, "created with salary of",self.salary)
    
    #Abstract Method
    @abstractmethod
    def work(self):
        #print("General work")
        pass
        
    #Method
    def recRoom(self):
        print("Having Fun!")
        
class HR(Employee):    
    
    #Overwrite abstract method 
    def work(self):
        print("Specific HR work")
        
    def organizeEvent(self):
        print("Organize event")
        
class Engineer(Employee):
    
    #Overwrite abstract method
    def work(self):
        print("Engineer engineering things on some software or something")
        
    def takeTraining(self):
        print("Taking engineer training")
        
'''
Main Program
'''
        
#Not possible to instantiate abstract class
#employee = Employee("David","120000")

hr = HR("Julieta","32154")
hr.work()
hr.recRoom()

print()

engineer = Engineer("Jorge", "120000")
engineer.work()
engineer.recRoom()
        
