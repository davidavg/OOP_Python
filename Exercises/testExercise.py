
'''
Created on Nov 05, 2018

@author: jose aperez 
'''

#import abstract library
from abc import abstractmethod, ABC


'Class Declaration Person'
class Person(ABC):
    
    'Constructor declaration'
    def __init__(self,name):
       
        'Class variables'
        self.name = name
 
    
    'Method talk'    
    def talk(self, name):
        print("Words = " + str(name))
    
    'Method hobby'   
    @abstractmethod
    def hobby(self):
        pass


'Class Declaration Teacher'
class Teacher(Person):
     
    'Constructor declaration'
    def __init__(self,signature):
        
        'Class variables'
        
        'Private'
        self.__name = name
        self.signature = signature
    
    'Method hobby'    
    def hobby(self):
        print("My hobby is to read")
        
    'Method teach'    
    def teach(self):
        print(str(name)+" is giving "+ str(signature) + " class")
        
    'Getter' 
    def getName(self):
        return self.__name
    
    'Setter'
    def setName(self,Newvalue):
        self.__name = Newvalue
        
'Class Declaration Engineer'
class  Engineer(Person):

    'Method hobby'    
    def hobby(self):
        print("My hobby is to play video games")
        
   
'''

Main program
'''
'Save variables'
name= str(input("Please write your name: "))


'Create Object'
#PersonObj = Person(name)
EngineerObj = Engineer(name)



'Create Class Object Teacher'
TeacherObj = Teacher(name)
TeacherObj.teach()

'Print Variables from Object'

#print("Accediendo a name desde Object Person = " + str(PersonObj.name))

print("Accediendo a name desde Object Engineer = " + str(EngineerObj.name))

'Print encapsulated name'
print("Accediendo a variable encapsulada:", TeacherObj.getName())

'Change encapsulated name value'
TeacherObj.setName("New name value")
print("Accediendo a variable con valor nuevo:", TeacherObj.getName())
