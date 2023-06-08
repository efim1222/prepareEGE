f = open('24.txt')
s = [x for x in f]
s = ''.join(s)
s = s.split('D')
n = list(map(len, s))
nsum = []
for x in range(len(n) - 1):
    v = n[x] + n[x + 1]
    nsum.append(v)
print(max(nsum) + 1)