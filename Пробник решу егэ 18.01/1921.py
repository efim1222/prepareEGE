from functools import lru_cache
@lru_cache(maxsize=None)


def f(n, m):
    # нужное число камней в 2 кучах
    if n + m >= 88:
        return 0
    # загоним все ходы, кол-во ходов, все возможные ходы
    a = [f(n + 1, m), f(n * 3, m), f(n, m + 1), f(n, m * 3)]
    # 
    c = [t for t in a if t <= 0]
    if c:
        r = -max(c) + 1
    else:
        r = -max(a)
    return r
for x in range(1, 72):
    t = 6
    if f(t, x) < 0:
        print(x, f(t, x))

# "-1" выигрывает Ваня 1 ходом
# "-2" выигрывает Ваня 2 ходом и т.д.
# "+1' выигрвает Петя 1 ходом и т.д.