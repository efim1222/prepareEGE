from functools import lru_cache
@lru_cache(maxsize=None)
def F(a, b):
    if a > b: return 0
    if a ==b: return 1
    if a < b: return F(a + 2, b) + F(a *5, b)
print(F(2, 50))