# 181)	Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, 
# всего не более чем из 10**6 символов. 
# Определите максимальное количество идущих подряд символов, среди которых не более одной точки.
with open('24-181.txt') as a:
    s1 = ''.join(a)
    s1 = s1.split('.')
    n = list(map(len, s1))
    nsum = []
    for x in range(len(n) - 1):
        v = n[x] + n[x + 1]
        nsum.append(v)
    print(max(nsum) + 1)