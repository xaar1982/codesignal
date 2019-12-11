def isIPv4Address(inputString):
    parsed_ip = inputString.split(".")
    try:
        ip = list(map(int ,parsed_ip))
    except ValueError:
        return False
    if (len(parsed_ip) != 4):
        return False
    check = [False for x in range(len(ip)) if ip[x] > 255]
    if check.__contains__(False):
        return False
    else:
        return True
