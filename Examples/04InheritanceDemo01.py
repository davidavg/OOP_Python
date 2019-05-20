'''
Created on Aug 6, 2018

@author: david avalos
'''

'''
1.Make Employee super class
2.Send especial parameters in HR object creation
3.Try Employee's methods with HR object
'''

#Class creation
class Employee:
   
    #Constructor declaration 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("Employee", self.name, "created with salaray of",self.salary)
    
    #Method
    def work(self):
        print("General employee work")
        
    #Method
    def recRoom(self):
        print("Having Fun!")
   
#Class creation    
class HR(Employee):
    
    #Method
    def organizeEvent(self):
        print("Organize event")

'''
Main Program
'''
        
print("Objects creation:")              
#Objects creation
david = Employee("David",10000)
hr = HR("Julieta",123020)

print("\nEmployee's Methods call:")

#Employee's methods call
david.work()
david.recRoom()

print("\nHR's Methods call:")

#HR's methods call
hr.work()
hr.recRoom()
hr.organizeEvent()