# То же самое только с 130-иричной системой счисления
# 355)	(А. Богданов) Операнды арифметического выражения записаны в системе счисления с основанием 13.
# 8x121₁₃ – 7x575₁₃
# В записи чисел переменной x обозначена неизвестная цифра из алфавита 13-ричной системы счисления. 
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 19. 
# Для найденного значения x вычислите частное от деления значения арифметического выражения на 19 и укажите его в ответе 
# в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно. 
# 
for x in range(130):
    t1 = 8*130**4 + x*130**3 + 1*130**2 + 2*130**1+ 1*130**0
    t2 = 7*130**4 + 5*130**3 + x*130**2 + 7*130**1 + 5*130**0
    if (t1 - t2) % 19 == 0:
        print((t1 - t2) / 19)