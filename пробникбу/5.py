def f(n):
    n8 = oct(n)[2:]
    n8m = []
    for x in n8:
        if int(x) % 2 == 0:
            n8m.append(str(int(x)*2))
        else:
            n8m.append(x+x)
    n8s = ''.join(n8m)
    return n8s
    
    
for n in range(10, 100):
    if f(n)[-1] == '1':
        print(n, f(n))

