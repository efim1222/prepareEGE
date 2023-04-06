def f(n):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = '1' + n2 + '00'
    else:
        ns = bin(sum(int(i) for i in n2))[2:]
        n2 = n2 + ns
    return int(n2, 2)


for x in range(1, 1000):
    if f(x) > 190:
        print(x)