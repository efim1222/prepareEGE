a = '0123456789ABCDEFG'
for x in a:
    t1 = int('149'+x+'3', 17)
    t2 = int(x + '612', 17)
    t3 = int(x + '54' + x, 17)
    if (t1 + t2 - t3) % 7 == 0:
        print(x)
        