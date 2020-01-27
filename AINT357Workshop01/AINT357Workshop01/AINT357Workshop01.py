
#The following are examples of constructs within Python 3.7

#1. Example of indentation format within Python:

def test():
    print("Hello, world!")

test() #Run the method

#2. Example of variable declaration and arithmetic operations:

#Declaring an integer variable:
numVar = 10
#Declaring a string variable:
stringVar = "Hello"
#Declaring a double variable:
doubleVar = 10.0
#Declaring a boolean variable:
booleanVar = True

#Example of calculation using Python:
calcAnswer = 10 / 3 #Will divide (answer will be 3.33333...)
print(calcAnswer) #Print the answer
calcAnswer = 10 % 3 #Modulus function: will find remainder of calculation (remainder of 10 / 3 = 1)
print(calcAnswer) #Print the answer

#3. For and while loops:

#Example For loop (uses N-1 indexing):
for x in range(5):
    print("loop iteration " + str(x)) #Print the current loop iteration 

#For loop using array
cars = ["Audi", "Toyota", "Peugeot"]

for y in cars:
    print(y)

#While loop example
startNum = 1 #Specify the start definition in the while loop

while startNum < 3:
    print("While loop test")
    startNum = startNum + 1 #++ doesn't work in Python it seems

#4. Booleans in Python:

#Booleans come in many forms. Certain comparisons will return true or false
print(9 > 2) #Will return true
print(9 < 2)  #Will return false

#The bool() function returns a true or false based on its parameters
#All strings will return true, and all numbers will return true except 0. All data structures will return true unless empty.

bool(0) #Returns false
bool(1) #Returns true
bool("Hello") #Returns true


#5. Conditional statements:
#The conditional statements in Python are if, elif, else, and, and or

#if statement example:
if (10 == 10):
    print("True!")

#elif statement example:
if (10 == 9):
    print("Nope")
elif 10 != 9:
    print("True")

#else statement example
if (10 == 9):
    print("False")
else:
    print("True")

#and statement example
if (10 == 10 and 9 == 9):
    print("True")

#or statement example
if (10 == 10 or 9 == 9):
    print("True")

#6. Functions/procedures with parameters and return values:

#Function/Method/Procedures example
def calculateSquare(numToSquare):
    return numToSquare * numToSquare

print(calculateSquare(2))

#7. Lists, arrays, dictionaries, tuples, sets:

#Lists
#Declaring a list:
newList = ["Car", "Pen", "Spoon"]

#Print all items in list:
print(newList)

#Print specific item in list:
print(newList[0])

#====================
#TODO: ADD MORE HERE
#====================

#Arrays
#Declaring an array:

#Declare array
newArray = [1, 2, 3]

#Add an element to the end of the array
newArray.append(4)

#Iterate through and print results:
for x in newArray:
    print(x)


#Dictionaries:
#Dictionaries are a data structure which is unordered, changeable, and indexed. They have both keys and values

#Example dictionary:
newDictionary = {
    "Animal" : "Cat",          #Mapping the value of cat to the attribute animal
    "Breed"  : "Russian Blue", #Mapping the value Russian Blue to the attribute breed
    "Age"    : "4"             #Mapping the value of 4 to the attribute age
}

#Printing dictionary:
print(newDictionary)

#Getting specific attribute of the dictionary by calling the key/attribute:
print(newDictionary["Animal"]) #Will output Cat

#Can also use a .get() method to obtain the value from a key/attribute:
print(newDictionary.get("Animal")) #Will output Cat

#Change the value of an attribute/key:
newDictionary["Animal"] = "Dog" #The animal attribute/key will now have the value of Dog

#Print all KEYS/ATTRIBUTES in the dictionary:
for x in newDictionary:
    print(x)

#Print all VALUES of the dictionary:
for x in newDictionary:
    print(newDictionary[x])

#Check if a specific key is in the dictionary:
if "Breed" in newDictionary:
    print("Key is present in this dictionary")

#Add new item to dictionary by adding a new index key/attribute and then adding its value:
newDictionary["Gender"] = "Female" # Adds "Gender" : "Female" to the dictionary

#Remove an item from the dictionary:
newDictionary.pop("Animal") #Remove the animal attribute/key and its value from the dictionary

#Tuples:



#8. I/O to/from console:

#Input:
storedInput = input("OPTIONAL: A string can appear here to prompt input!")

#Output:
print(storedInput) 

#9. I/O to/from files:

#================================
#TODO: MAYBE ENRICH THIS SECTION
#================================

#Taking input from a file:
#(Commented out so as not to create the file currently)
#streamVar = open("someTextDocument.txt", w+) #Takes 2 arguments, the text document to manipulate and the operations we wish to do on it. The potential options are:

# 'w' = Allows us to write to the file (Will create the file if it does not already exist)
# 'w+' = Allows us to read and write to the file (Will create the file if it does not already exist)
# 'r' = Allows us to read from the file (Error if the file doesn't exist)
# 'a' = Allows us to append the file (creates the file if it doesn't already exist)
# 'x' = Creates the file if it doesn't already exist (Error if it does)

#10. Modules:

#Simply put, a module is just a group of Python code. Much like a package in Java, it can define functions, classes, and variables.
#Python modules can be imported, for example:

import math #Imported the math module

a = math.factorial(3) #Finds the factorial of 3
print(a)

#11. Classes/OO:

#Classes in Python act much like classes in other programming languages; they are templates from which an object can be created:

#Simple class with variables, constructor and method

class MyClass: #Class definition

    x = 5 #variables/field
    y = 0 #variables/field

    def __init__(self): #Constructor
        self.y = 9 #Set value of field to 9

    def compare(a, b): #Compare method
        if (a == b):
            print("They are the same number")
        elif (a < b):
            print("The first number is smaller than the second")
        elif (a > b):
            print("The first number is bigger than the second")


#Instancing the class:

objectOne = MyClass

print(objectOne.compare(9, 9))





