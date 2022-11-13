import itertools as it 
a = list(it.product('ЧЕРПАШК', repeat=9))
mas = []
for x in a:
    b = ''.join(x)
    mas.append(b)
for i in range(len(mas)):
    if mas[i] == 'ЧЕРЕПАШКА':
        print(i + 1)