# 422)	(А. Богданов) На числовой прямой дан отрезок Q = [29; 47].  
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится 
# без остатка на натуральное число m». Определите наименьшее натуральное число A, 
# такое что выражение
# ( ¬ДЕЛ(x, 3) ∧ x ∉ {48, 52, 56}) → (( |x – 50| ⩽ 7) → ( x in Q )) ∨ (x & A = 0)
# тождественно истинно (то есть принимает значение 1 при любом натуральном значении переменной x)?
t = [48, 52, 56]
q = range(29, 48)
for a in range(1, 200):
    f = 0
    for x in range(1, 200):
        if (  ((x % 3 != 0) and (not x in t)) <= ((abs(x - 50) <= 7) <= (x in q)) or (x & a == 0)    ) == False:
            f = 1
    if f == 0:
        print(a)