#В файле содержатся цепочка из символов A, B, C, D, E.
# Найдите максимальную подцепочку, состоящую из символов C
s = open('24_1.txt').readline()
t = 0
maxt = 0
for x in s:
    if x == 'C':
        t += 1 
        maxt = max(maxt, t)
    else:
        t = 0
print(maxt)
#69
#or
t = ''
while t in s:
    t += 'C'
print(len(t) -  1)
#69
#or
s = s.replace('A', '*').replace('B', '*').replace('D', '*').replace('E', '*')
s = s.split('*')
print(len(max(s, key = len)))
#or
s = list(map(len, s))
print(max(s))
#69