def allLongestStrings(inputArray):
    longest = 0
    longest_array = []
    l = len(inputArray)
    for i in range(l):
        if (len(inputArray[i]) >= longest):
                longest = len(inputArray[i])
    for i in range(l):
        if (len(inputArray[i]) == longest):
                longest_array.append(inputArray[i])
        
    return longest_array
