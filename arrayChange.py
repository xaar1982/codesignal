def arrayChange(inputArray):
    count = 0
    for i in range(len(inputArray) - 1):
        if inputArray[i] >= inputArray[i+1]:
            single_moves = inputArray[i] - inputArray[i+1] + 1
            inputArray[i + 1] += single_moves
            count += single_moves

    return count
