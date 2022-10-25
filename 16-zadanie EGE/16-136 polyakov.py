import sys
sys.setrecursionlimit(2000)
def F(n):
    if n < 3:
        return 1
    if n > 3:
        return F(n-1) + F(n-2)
print((F(1006) - F(1004))/F(1005))