'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
Hints:
Use __init__ method to construct some parameters'''
#Didn't see why i needed to use the init method 
class string():
    def inputstring(self): #self is used to differentiate btw instance and local variables
        self.s=input()

    def printstring(self): 
        print(self.s)

ob= string() #creating obj 
ob.inputstring() #calling inputstring method from class
ob.printstring() #caling printstring method from class


        
