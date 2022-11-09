a = 6 ** 203 + 5 * 6 ** 405 - 3 * 6 ** 144 + 76
a6 = ''
a6m = []
while a >0:
    a6 = str(a % 6) + a6
    a //= 6
for x in a6:
    a6m.append(int(x))
print(sum(a6m))