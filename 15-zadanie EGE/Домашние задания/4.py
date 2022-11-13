for A in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        if ( ((x % A == 0) and (not(x % 27 == 0))) <= (not(x % 36 ==0))) == False:
            flag = 0
            break
    if flag == 1:
        print(A)