f = open('17 (1).txt')
a = [int(x) for x in f]
mx = c = 0
sr = []
srznach = 0
for x in range(len(a)):
    if a[x] % 2 != 0:
        sr.append(a[x])
srznach = sum(sr) / len(sr)
for x in range(len(a) - 1):
    if (( a[x] % 5 == 0 and a[x + 1] % 5 != 0 ) \
        or ( a[x] % 5 != 0 and a[x + 1] % 5 == 0 ) \
        or ( a[x] % 5 == 0 and a[x + 1] % 5 == 0)) and \
            \
            ((a[x] < srznach and a[x + 1] > srznach) or \
                (a[x] > srznach and a[x + 1] < srznach) or \
             (a[x] < srznach and a[x + 1] < srznach)):
                c += 1
                mx = max(mx, a[x] + a[x + 1])
print(c, mx)