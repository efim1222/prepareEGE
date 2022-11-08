a = 4*(125**4) - 25**4 + 9
a1 = ''
while a > 0:
    a1 = str(a % 5) + a1
    a //= 5
print(a1.count('4'))