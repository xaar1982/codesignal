def isLucky(n):
    dl = len(str(n))
    half = int(dl/2)
    int_to_string = str(n)
    first_half = list(map(int, int_to_string[:half]))
    second_half = list(map(int, int_to_string[half:]))
    if sum(first_half) == sum(second_half):
        return True
    else:
        return False
