# 131)	Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому числу.
# Найдите все натуральные числа, принадлежащие отрезку [106732567; 152673836]
# и имеющие ровно три нетривиальных делителя.
# Для каждого найденного числа запишите в ответе само число и его наибольший нетривиальный делитель.
# Найденные числа расположите в порядке возрастания.

for number in range(106732567, 152673837):
    сount = 0
    if number ** 0.5 == int(number ** 0.5):
        for delitel in range(1, int(number ** 0.5)):
            if number % delitel == 0:
                сount += 1
                t = number//delitel
                if сount > 2:
                    break
        if сount == 2:
            print(number, t)