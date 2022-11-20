from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
# Устанавливает размер рекурсии
@lru_cache(maxsize=None)
# Не считает член рекурсии, если он уже известен


def a(n):
    if n <= 2:
        return 1
    else:
        return a(n-1) + a(n-2)
print(a(1000))