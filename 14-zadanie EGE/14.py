for x in '0123456789ABCDE':
    r = int('123' + x + '5', 15) + int('1' + x + '233', 15)
    if r%14==0:
        print(r//14)
