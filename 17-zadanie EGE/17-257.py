with open('17-257.txt') as a:
    s = [int(x) for x in a]
    res7 = []
    res13 = []
    for x in range(len(s)):
        if s[x] % 7 == 0:
          res7.append(s[x])
        if s[x] % 13 == 0:
            res13.append(s[x])
    min7 = min(res7)
    min13 = min(res13)
    if min7 > min13:
        print(len(res7), max(res7))
    else:
        print(len(res13), max(res13))
