x = int('200',5) - int('60',8)
x6 = ''
while x>0:
    x6 = str(x%6)+x6
    x //=6
print(x6)