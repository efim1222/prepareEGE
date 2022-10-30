# Сколько значащих нулей в двоичной записи числа 8^740 — 2^
# 900 + 7?

number_decimal = 8 ** 740 - 2 ** 900 + 7
number_binary = str(bin(number_decimal)[2:])
print(number_binary.count('0'))