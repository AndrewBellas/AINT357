# Andrew Bellas
# AINT357 - Recursion


# Question 1 - Compute the sum of the numbers from 1 to N:

def sumToN(n):
    if(n <= 1):
        return 1
    return n + sumToN(n - 1)


print(sumToN(989))

# Question 2 - Compute the maximum of an array of integers:

def computeMaxArray(inputArray, arraySize):
    
    if(arraySize == 1):
        return inputArray[0]
    return max(inputArray[arraySize - 1], computeMaxArray(inputArray, arraySize - 1))


arrayInput = [57, 52, 67, 93]

print(computeMaxArray(arrayInput, 4))

# Question 3 - Compute the maximum of an array of integers using tail recursion:
# See question 2 (implements tail recursion)

# Question 4 - Implement a binary search tree with depth first traversal for insertion of elements and printing of the tree:

def DepthFirstSearch(inputData, nodes):
    if (inputData != null):
        return 0