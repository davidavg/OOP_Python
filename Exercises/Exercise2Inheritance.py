'''
Created on Aug 13, 2018

@author: david avalos
'''

class Person:

    def __init__(self, name):
        self.name = name
    
    def talk(self, words):
        print(self.name, "says:", words)
        
    def hobby(self):
        print("My hobby is to watch movies")
        
class Teacher(Person):
    
    def __init__(self, name, signature):
        self.name = name
        self.signature = signature
        
    def hobby(self):
        print("My hobby is to read")
        
    def teach(self):
        print(self.name,"is giving",self.signature,"class")
        
class Engineer(Person):
    
    def hobby(self):
        print("My hobby is to play video games")

myPerson = Person("David")
myPerson.talk("Hello! :)")
myPerson.hobby()

print()

myTeacher = Teacher("Jorge","Math")
myTeacher.talk("Ready for my class?")
myTeacher.hobby()
myTeacher.teach()

print()

myEngineer = Engineer("Genaro")
myEngineer.talk("Don't know what to say D:")
myEngineer.hobby()


