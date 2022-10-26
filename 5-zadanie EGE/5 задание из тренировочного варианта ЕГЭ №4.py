n = 97
n2 = str(bin(n)[2:])
print(n2)
c = []
for x in n2:
    c.append(int(x))
summa = sum(c)
print(c, summa)
if n2[-1] == '0':
    n2 = n2 + str(bin(summa)[2:])
    print(n2)
if n2[-1] == '1':
    n2 = '1' + n2 + '00'
    print(n2)


