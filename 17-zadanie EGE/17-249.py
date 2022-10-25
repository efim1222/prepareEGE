with open('17-243.txt') as a:
    b = [int(x) for x in a]
    res211 = []
    res = []
    for x in range(len(b)):
        if b[x] % 211 == 0:
            res211.append(b[x])
    max211 = max(res211)
    for x in range(len(b)-1):
        if (b[x] > max211 or b[x+1] > max211) and (str(b[x]).count('1') >= 1 or str(b[x+1]).count('1') >= 1):
            res.append(b[x] + b[x+1])
print(len(res))
print(min(res))