a_s = []
# массив с А-шками
for a in range(1, 10000):
    flag = 0 
    # флажок ложности
    for x in range(1, 10000):
        if ( (x % a == 0) <= ((x % a == 0) <= ((x % 34 == 0) and (x % 51 == 0)) ) ) == False:
            flag = 1
            # А-шка не подошел, заканчиваем цикл
            break
    if flag == 0:
        # а-шка подошла, записываем в массив 
        a_s.append(a)
print(min(a_s))