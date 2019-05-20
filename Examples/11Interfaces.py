'''
Created on Aug 6, 2018

@author: david avalos
'''
#import abstract library
from abc import abstractmethod, ABC

class Employee(ABC):
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("Employee", self.name, "created with salary of",self.salary)
    
    @abstractmethod
    def work(self):
        pass
        
    @abstractmethod
    def takeTraining(self):
        pass
        
class HR(Employee):    
    
    def work(self):
        print("Specific HR work")
        
    def takeTraining(self):
        print("Taking HR training")
        
class Engineer(Employee):
    
    def work(self):
        print("Engineer engineering things on some software or something")
        
    def takeTraining(self):
        print("Taking engineer training")
        
'''
Main Program
'''
        
hr = HR("Julieta","32154")
hr.work()
hr.takeTraining()

print()

engineer = Engineer("David", "120000")
engineer.work()
engineer.takeTraining()
        
