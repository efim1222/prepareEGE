with open('17 (2).txt') as a:
    res = []
    s = [int(x) for x in a]
    oddm = []
    for x in s:
        if x % 2 != 0:
            oddm.append(x)
    srarph = sum(oddm) / len(oddm)
    for x in range(len(s) - 1):
        if (s[x] % 5 == 0 and s[x + 1] < srarph) or \
            (s[x + 1] % 5 == 0 and s[x] < srarph):
                res.append(s[x] + s[x + 1])
print(len(res), max(res))