# 26)	Напишите программу, которая ищет среди целых чисел, 
# принадлежащих числовому отрезку [78920; 92430], 
# числа, имеющие ровно 5 различных делителей. 
# Выведите эти делители для каждого найденного 
# числа в порядке возрастания.
for x in range(78920, 92431):
    delit = []
    for y in range(1, x + 1):
        if x % y == 0:
            delit.append(y)
    if len(delit) == 5:
        print(delit)
                