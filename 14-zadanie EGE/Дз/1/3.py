a = 3**3 * 7**69 - 70
a7 = ''
while a > 0:
    a7 = str(a % 7) + a7
    a //= 7
print(a7.count('4'))