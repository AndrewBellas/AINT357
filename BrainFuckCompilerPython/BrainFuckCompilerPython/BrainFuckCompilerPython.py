
#BrainFuck Compiler - Python Implementation
# Andrew Bellas

#cellSize = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cellSize = []


cellPointerIdx = 0

code = ">>++."

def populateBytes():
    for i in code:
        cellSize.append(0)
    print(cellSize)



for x in code:

    populateBytes()

    if (x == ">"):
        cellPointerIdx = cellPointerIdx + 1

    elif (x == "<"):
        if (cellPointerIdx >= 0):
            cellPointerIdx = cellPointerIdx - 1

    elif (x == "+"):
        cellSize[cellPointerIdx] = cellSize[cellPointerIdx] + 1
    
    elif(x == "-"):
        cellSize[cellPointerIdx] = cellSize[cellPointerIdx] - 1

    elif(x == "."):
        print(cellSize[cellPointerIdx])

    elif(x == ","):
        a = input()
        cellSize[cellPointerIdx] = a

    #TODO: Add loop control
