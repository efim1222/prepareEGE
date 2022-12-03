alp8 = '01234567'
for x in alp8:
    for y in alp8:
        t = int(y + '04' + x + '5', 11) + int('253' + x + y, 8)
        if t % 117 == 0:
            print(t, t // 117)