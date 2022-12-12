from functools import lru_cache
@lru_cache(None)

def f(n):
    if n >= 165:
        return 0
    moves = [f(n + 1), f(n * 2)]
    lose = [t for t in moves if t <= 0]
    if lose:
        res = -max(lose) + 1
    else:
        res = -max(moves)
    return res
for n in range(1, 168):
    print(n, f(n))