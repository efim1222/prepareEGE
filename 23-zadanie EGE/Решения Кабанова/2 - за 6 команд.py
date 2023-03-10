# 103) Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три команды,
# которым присвоены номера:
# 1 Прибавить 1
# 2 Прибавить 2
# 3 Умножить на 2
# Сколько существует программ, состоящих из 6 команд, для которых при исходном числе 1
# результатом является число 20?
def f(s, e, steps):
    if s > e: return 0
    if s == e and steps == 6: return 1
    if s == e and steps != 6: return 0
    if s < e: return f(s + 1, e, steps + 1) + f(s + 2, e, steps + 1) \
        + f(s * 2, e, steps + 1)
        
print(f(1,20,0))