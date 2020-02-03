
#BrainFuck Compiler - Python Implementation
#Andrew Bellas - 2019

#Initialise list of finite tape
cellSize = []

#The data pointer index for the operations
cellPointerIdx = 0

#Enter your code here
code = ">>++.,"


#Append the length of the byte list for the length of the code string, and set the default values of the cells in the finite tape to zero
def populateBytes():
    for i in code:
        cellSize.append(0)

populateBytes()


#Define method "populateBytes" -> creates the finite tape for the program
def showBytes():
    print(cellSize)



#Simple parser for the code string
for x in code:

    #Populate the finite tape = to size of the code string to execute
    showBytes()

    #If the code string has character ">", increment the data pointer by 1
    if (x == ">"):
        cellPointerIdx = cellPointerIdx + 1

    #If the code string has character "<", decrement the data pointer by 1
    elif (x == "<"):

        #Check the data pointer location on the tape is not going to go out of bounds
        if (cellPointerIdx >= 0):
            cellPointerIdx = cellPointerIdx - 1

    #if the code string has character "+", increment the value in the cell the data pointer is currently pointing to
    elif (x == "+"):
        cellSize[cellPointerIdx] = cellSize[cellPointerIdx] + 1
    
    #If the code string has character "-", decrement the value in the cell the data pointer is currently pointing to
    elif(x == "-"):
        cellSize[cellPointerIdx] = cellSize[cellPointerIdx] - 1

    #If the code string has character ".", output the value of the cell the data pointer is currently pointing to (MAY NEED WORK)
    elif(x == "."):
        print(cellSize[cellPointerIdx])

    #If the code string has character ",", take an input and store the input in the cell the data pointer is currently pointing to 
    elif(x == ","):
        a = input()
        cellSize[cellPointerIdx] = int(a)


    #TODO: Add loop control



#EXIT LOOP:

#Output final state of the tape (after loop iterations are complete)
print()
print("Final state of tape")
showBytes()