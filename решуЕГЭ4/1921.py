from functools import lru_cache
@lru_cache(maxsize=None)


def f(n):
    if n >= 102:
        return 0
    a = [f(n + 1), f(n * 2)]
    c = [t for t in a if t <= 0]
    if c:
         r = -max(c) + 1
    else:
        r = -max(a)
    return r

for n in range(1, 102):
    if f(n) == -1 or f(n) == -2:
        print(n)
        
        
# "-" выигрывает Ваня
# "+' выигрвает Петя