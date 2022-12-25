# +5
# *2
# +10
# Но каждая третья программа не равна +10
def f(a, b, c):
    c += 1
    if a == b:
        return 1
    if a > b:
        return 0
    if a < b:
        if c % 3 == 0:
            return f(a + 5, b, c) + f(a * 2, b, c)        
        else:
            return f(a + 5, b, c) + f(a * 2, b, c) + f(a + 10, b, c)
print(f(10, 40, 0))