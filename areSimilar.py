def areSimilar(a, b):
    c = 0
    d = set(a)
    e = set(b)
    f = d & e
    if (d == e):
        if (len(d) == len(e)):
            for i in range(len(a)):
                if a[i] == b[i]:
                    continue
                else:
                    c+=1
            if c > 2:
                return False
            elif c == 2:
                return sorted(a) == sorted(b)
            else:
                return True
        else:
            return False
    else:
        return False
