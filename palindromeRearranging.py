from collections import Counter

def palindromeRearranging(inputString):
    return len([v for v in Counter(inputString).values() if v % 2 == 1]) <= 1
