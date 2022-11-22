from functools import lru_cache
@lru_cache(maxsize=None)

def F(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a < b:
        return F(a + 1, b) + F(a + 3, b) + F(a + 6, b)
print(F(21, 30)) 
# 25 otevet