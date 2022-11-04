s = 81**17 + 3**24 - 45
s9 = ''
while s > 0:
    s9 = str(s % 9 ) + s9
    s //= 9 
print(s9.count('8'))
    