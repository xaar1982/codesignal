def sortByHeight(a):
    sorted_list = []
    tree_list = []
    for i in range(len(a)):
        if (a[i] == -1):
            tree_list.append(i)
        else:
            sorted_list.append(a[i])
    sorted_list = sorted(sorted_list)
    for tree in range(len(tree_list)):
        sorted_list.insert(tree_list[tree], -1)
    
    return sorted_list
