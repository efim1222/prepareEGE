from functools import lru_cache
@lru_cache(maxsize=None)
def F(a, b):
    if a > b or a == 13:
        return 0
    if a == b:
        return 1
    if a < b:
        return F(a + 1, b) + F(a + 2, b) + F(a * 3, b)
    
print(F(1, 9) * F(9, 15))