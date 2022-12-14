
# 69)	Исполнитель Июнь15 преобразует число на экране. 
# У исполнителя есть две команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Умножить на 2
# Первая команда увеличивает число на экране на 1, 
# вторая умножает его на 2. Программа для исполнителя Июнь15 
# – это последовательность команд. Сколько существует программ, 
# для которых при исходном числе 2 результатом является число 33 
# и при этом траектория вычислений содержит число 16 и 
# не содержит число 30?



from functools import lru_cache
@lru_cache(maxsize=None)

def F(a, b):
    if a > b or a == 30:
        return 0
    if a == b:
        return 1
    if a < b:
        return F(a + 1, b) + F(a * 2, b)
print(F(2, 16) * F(16, 33))