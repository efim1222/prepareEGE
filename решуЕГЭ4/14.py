a = '0123456789AB'
for x in a:
    for y in a:
        s1 = x + '231' + y
        s2 = '78' + x + '98' + y
        t = int(s1, 12) + int(s2, 14)
        if t % 99 == 0:
            print(x, y, t, t // 99)
        