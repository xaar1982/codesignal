def arrayMaximalAdjacentDifference(inputArray):
    biggest = 0
    for x in range(len(inputArray) - 1):
        if (abs(inputArray[x] - inputArray[x+1]) > biggest):
            biggest = abs(inputArray[x] - (inputArray[x+1]))
        else:
            continue
    return biggest
