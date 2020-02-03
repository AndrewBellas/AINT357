
#BrainFuck Compiler - Python Implementation
# Andrew Bellas

cellSize = [30000]

cellPointerIdx = 0

code = ">+"

for x in code:
    if (x == ">"):
        cellPointerIdx = cellPointerIdx + 1

    elif (x == "<"):
        if (cellPointerIdx >= 0):
            cellPointerIdx = cellPointerIdx - 1

    elif (x == "+"):
        cellSize[cellPointerIdx] = cellSize[cellPointerIdx] + 1
    
    elif(x == "-"):
        cell_size[cellPointerIdx] = cellSize[cellPointerIdx] - 1

    elif(x == "."):
        print(cellSize[cellPointerIdx])

    elif(x == ","):
        a = input()
        cellSize[cellPointerIdx] = a

    #TODO: Add loop control