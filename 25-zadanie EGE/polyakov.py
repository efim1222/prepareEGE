for x in range(206, 10**8 + 1, 206):
    s = str(x)
    if s[0:3] == '123' and s[-1] == '6' and s[-2] == '5' and s[-3] in '02468' and s[-4] in '13579':
        print(x, x // 206)