f = open('17_7267.txt')
s = [int(x) for x in f]
smin = min(s)
c = cmax = 0
for x in range(len(s) - 1):
    if s[x] % 117 == smin or s[x + 1] % 117 == smin:
        c += 1
        cmax = max(cmax, s[x] + s[x + 1]) 