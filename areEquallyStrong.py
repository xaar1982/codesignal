def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    sum_my_weights = yourLeft + yourRight
    sum_friends_weights = friendsLeft + friendsRight
    count = 0
    all_arms = [yourLeft, yourRight, friendsLeft, friendsRight]
    heaviest_arm = max(all_arms)
    for i in range(len(all_arms)):
        if all_arms[i] == heaviest_arm:
            count+=1
        else:
            continue

    if (count == 1):
        return False
    
    elif (sum_my_weights == sum_friends_weights):

        return True
    else:
        return False
