t = 5 * 343 ** 8 + 4 * 49 ** 12 + 7 ** 14 - 98
t7 = ''
while t > 0:
    t7 = str(t % 7) + t7
    t //= 7
print(t7)