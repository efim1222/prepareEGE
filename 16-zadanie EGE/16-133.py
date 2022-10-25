import sys
sys.setrecursionlimit(4000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (3*n + 5) * F(n-1)
print(F(2073)/F(2070))

