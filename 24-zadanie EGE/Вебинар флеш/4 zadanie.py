#В файле содержатся цепочка из символов A, B, C, D, E.
# Найдите максимальную подцепочку, среди которых два соседних элемента различны
s = open('24_1.txt').readline()
t = 1
maxt = 0
for x in range(len(s) - 1):
    if s[x] != s[x + 1]:
        t += 1 
        maxt = max(maxt, t)
    else:
        t = 1
print(maxt)