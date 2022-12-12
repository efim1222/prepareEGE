f = open('17-345.txt')
s = [int(x) for x in f]
maxmin52 = []
razn = 0
res = []
for x in s:
    k = str(x)
    if k[-1] == '2' and k[-2] == '5':
        maxmin52.append(int(k))
razn = max(maxmin52) - min(maxmin52)
for x in range(len(s) - 1):
    if (s[x] < razn and s[x + 1] > razn) or (s[x] > razn and s[x + 1] < razn):
        res.append(s[x] + s[x + 1])
print(len(res), max(res))