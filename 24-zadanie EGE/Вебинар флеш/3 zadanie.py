#В файле содержатся цепочка из символов A, B, C, D.
# Найдите максимальную подцепочку, не содержащую D
s = open('24_3.txt').readline()
t = 0
maxt = 0
for x in s:
    if x != 'D':
        t += 1 
        maxt = max(maxt, t)
    else:
        t = 0
print(maxt)
#105
#or
s = s.replace('D', '*')
s = s.split('*')
print(len(max(s, key=len)))
#  ищет максимальный элемнт в списке по длине каждого элемента