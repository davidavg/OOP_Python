'''
Created on Oct 1, 2018

@author: david avalos
'''

#Declare variables
myString = "Hello World!"
myInt = 20
anotherInt = 123

#This is how we learned to concatenate numbers
print("This is my int: " + str(myInt))

print("This is my string: %s" % myString)

#This is a nother way to concatenate numbers
print("This is my int: %d " % myInt)

#This will throw an error
#print("Multiple ints %d, %d" % myInt, anotherInt)

#This is the correct way to concatenate multiple variables
print("Multiple ints: %d, %d" % (myInt, anotherInt))