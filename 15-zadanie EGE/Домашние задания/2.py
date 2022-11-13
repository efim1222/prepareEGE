for A in range(1000):
    flag = 1
    for x in range(1000):
        if ( (x & 33 == 0) or ((x & 58 == 0) <= (x & A != 0))) == False:
            flag = 0
            break
    if flag == 1:
        print(A)