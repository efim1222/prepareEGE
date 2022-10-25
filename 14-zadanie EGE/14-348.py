alph11 = '0123456789A'
alph12 = '123456789AB'
alph14 = '0123456789ABCD'
for x1 in alph11:
    for x2 in alph12:
        for x3 in alph14:
            if int('3364' + x1, 11) + int(x2 + '7946', 12) == int('55' + x3 + '87', 14):
                print(int('55' + x3 + '87', 14))