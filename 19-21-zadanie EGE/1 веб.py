def f(n):
    # нужное число камней в куче
    if n >= 30:
        return 0
    # загоним все ходы, кол-во ходов, все возможные ходы
    a = [f(n + 2), f(n * 3)]
    # 
    c = [t for t in a if t <= 0]
    if c:
        r = -max(c) + 1
    else:
        r = -max(a)
    return r
for i in range(1, 30):
    if f(i) == -1:
        print(i)
# "-" выигрывает Ваня
# "+' выигрвает Петя