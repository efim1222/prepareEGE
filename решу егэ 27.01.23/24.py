with open('inf_22_10_20_24.txt') as a:
    s = [x for x in a]
    c = 0
    for x in s:
        if x.count('E') > x.count('A'):
            c += 1
    