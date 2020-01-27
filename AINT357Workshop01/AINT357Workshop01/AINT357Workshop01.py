
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






