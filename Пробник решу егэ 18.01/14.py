alph = '0123456789ABCDEF'

for x in alph:
    s1 = '8' + x + '84' + x
    s2 = '78' + x + '34'
    t = int(s1, 16) + int(s2, 16)
    if t % 23 == 0:
        print(t // 23, t, x)
    