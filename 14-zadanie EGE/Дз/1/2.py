s = 7 * 6561 ** 46 + 8 * 729 ** 15 - 6 * 5832
s9 = ''
while s > 0:
    s9 = str(s % 9) 
    s //= 9
print(s9.count('7'))