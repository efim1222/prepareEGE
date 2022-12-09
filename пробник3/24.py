with open('inf_26_04_21_24.txt') as a:
    s = [str(x) for x in a]
    s1 = []
    for x in s:
        if x.count('G') < 25:
            s1.append(x)
    for y in s1