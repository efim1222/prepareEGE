for A in range(1000):
    flag = 1
    for x in range(1000):
        if ( (x & 39 == 0) or (not (x & 67 == 0)) or (x & A != 0)) == False:
            flag = 0
            break
    if flag == 1:
        print(A)