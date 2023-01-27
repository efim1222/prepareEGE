import sys
from functools import lru_cache
sys.setrecursionlimit(6000)
@lru_cache(maxsize=None)

def F(n):
    if n <= 2:
        return n + 1
    if n > 2:
        return F(n - 1) * F(n - 2)
print(F(4))