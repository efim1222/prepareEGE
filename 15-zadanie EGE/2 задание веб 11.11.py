a_s = []
# массив с А-шками
for a in range(1, 1000):
    flag = 0 
    # флажок ложности
    for x in range(1, 1000):
        if (((x & 7 != 0) <= ((x & a != 0) <= (x & 54 != 0))) \
            <= ((x & 27 == 0) and (x & a != 0) and (x & 7 != 0))) == True:
            flag = 1
            # А-шка не подошел, заканчиваем цикл
            break
    if flag == 0:
        # а-шка подошла, записываем в массив 
        a_s.append(a)
print(len(a_s))