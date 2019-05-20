'''
Created on Aug 13, 2018

@author: david avalos
'''

class Person:

    def __init__(self, name):
        self.name = name
    
    def talk(self, words):
        print(words)
        
    def hobby(self):
        print("My hobby is to watch movies")
        
class Teacher(Person):
    
    def __init__(self, name, signature):
        self.__name = name
        self.__signature = signature
        
    def hobby(self):
        print("My hobby is to read")
        
    def teach(self):
        print(self.__name,"is giving",self.__signature,"class")
        
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
        
        
class Engineer(Person):
    
    def hobby(self):
        print("My hobby is to play video games")

myPerson = Person("David")
myPerson.talk("Hello! :)")
myPerson.hobby()
print(myPerson.name)

print()

myTeacher = Teacher("Jorge","Math")
myTeacher.talk("Ready for my class?")
myTeacher.hobby()
myTeacher.teach()
#print(myTeacher.__name)
myTeacher.setName("Martin")
print(myTeacher.getName())


print()

myEngineer = Engineer("Genaro")
myEngineer.talk("Don't know what to say D:")
myEngineer.hobby()
print(myEngineer.name)


