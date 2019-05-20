'''
Created on Aug 6, 2018

@author: david avalos
'''

class Employee():
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("Employee", self.name, "created with salary of",self.salary)
    
    def work(self):
        #print("Generic employee work")
        pass
        
    def recRoom(self):
        print("Having Fun!")
        
class HR(Employee):    
    
    #def work(self):
    #    print("Specific HR work")
        
    def organizeEvent(self):
        print("Organize event")
        
class Engineer(Employee):
    
    def work(self):
        print("Engineer engineering things on some software or something")
        
    def takeTraining(self):
        print("Taking engineer training")
        
'''
Main Program
'''
        
employee = Employee("David","120000")
employee.work()

print()

hr = HR("Julieta","32154")
hr.work()
hr.recRoom()

print()

engineer = Engineer("Jorge", "120000")
engineer.work()
engineer.recRoom()
        
