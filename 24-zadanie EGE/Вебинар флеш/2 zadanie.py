#В файле содержатся цепочка из символов A, B, C, D.
# Найдите максимальную подцепочку, состоящую из символов A, B ИЛИ C
# в произвольном порядке
s = open('24_2.txt').readline()
t = 0
maxt = 0
for x in s:
    if x == 'C' or x == 'A' or x == 'B':
        t += 1 
        maxt = max(maxt, t)
    else:
        t = 0
print(maxt)
#72
#or
s = s.replace("A", "X").replace("B", "X").replace("C", "X").replace("D", "*").replace("E", "*")
s = s.split('*')
print(len(max(s, key=len)))
#  ищет максимальный элемнт в списке по длине каждого элемента