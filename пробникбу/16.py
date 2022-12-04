def F(n):
    if abs(n % 2 - 1) >= 1 and n > 0:
        print(abs(n-1))
    else:
        if n > 0:
            print(abs(n - 2 ))
            F(n - 2)
print(F(11))