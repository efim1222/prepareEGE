alph = '0123456789A'
for x in alph:
    for y in alph:
        t1 = int('7' + y +'23' + x + '5', 25)
        t2 = int('67' + x + '9' + y, 11)
        if (t1 + t2) % 131 == 0:
            print((t1 + t2) / 131) 
