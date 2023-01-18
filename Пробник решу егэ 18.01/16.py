import sys
from functools import lru_cache
sys.setrecursionlimit(6000)
@lru_cache(maxsize=None)

def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return F(n-2) + F(n-1)
print(F(8))