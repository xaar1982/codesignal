def makeArrayConsecutive2(statues):
    missing_statues = 0
    for i in range(min(statues),max(statues)):
        if statues.count(i):
            continue
        else:
            missing_statues+=1
    return missing_statues
