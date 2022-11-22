
from functools import lru_cache
@lru_cache(maxsize=None)

def F(a, b):
    if a > b or a == 10:
        return 0
    if a == b:
        return 1
    if a < b:
        return F(a + 1, b) + F(a * 2, b)
print(F(1, 25) * F(25, 28)) 
# 38 ответ