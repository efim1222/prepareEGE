a = (3 * (343 ** 8)) + (5 * (49 ** 12)) + (7 ** 15) -49
a1 = ''
while a:
    a1 = str(a % 7) + a1
    a = a // 7
print(a1)
print('0', a1.count('0'))
print('1', a1.count('1'))
print('2', a1.count('2'))
print('3', a1.count('3'))
print('4', a1.count('4'))
print('5', a1.count('5'))
print('6', a1.count('6'))

