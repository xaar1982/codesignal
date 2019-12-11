def adjacentElementsProduct(inputArray):
    maks = None
    iloczyn = None
    for i in range(len(inputArray)):
        if i < len(inputArray) - 1:
            iloczyn = inputArray[i] * inputArray[i+1]
            if iloczyn > maks:
                maks = iloczyn
    return maks
