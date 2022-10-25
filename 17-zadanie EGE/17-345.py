with open('17-345.txt') as a:
    b = [int(x) for x in a]
    res52 = []
    res = []
    for x in range(len(b)):
        if str(b[x])[-1] == '2' and str(b[x])[-2] == '5':
            res52.append(b[x])
    raznost = max(res52) - min(res52)
    for x in range(len(b)-1):
        if (b[x] < raznost and b[x+1] >= raznost) or (b[x] >= raznost and b[x+1] < raznost):
            res.append(b[x] + b[x+1])
print(len(res))
print(max(res))