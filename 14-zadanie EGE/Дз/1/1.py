s = 5 * 36**7 + 6**10 -36
s6 = ''
while s > 0:
    s6 = str(s % 6) + s6
    s //= 6
print(s6.count('5'))