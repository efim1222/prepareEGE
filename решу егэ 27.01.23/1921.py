from functools import lru_cache
@lru_cache(maxsize=None)

def f(n):
    # нужное число камней в куче
    if n >= 70:
        return 0
    # загоним все ходы, кол-во ходов, все возможные ходы
    a = [f(n + 1), f(n + 4), f(n * 5)]
    # 
    c = [t for t in a if t <= 0]
    if c:
        r = -max(c) + 1
    else:
        r = -max(a)
    return r
for n in range(1, 70):
    if f(n) == -1 or f(n) == -2:
        print(n)
# "-" выигрывает Ваня
# "+' выигрвает Петя