from math import factorial
import sys
sys.setrecursionlimit(100000)
def F(n):
    if n >= 5000:
        return factorial(n)
    if 1 <= n < 5000:
        return (2 * F(n+1))/(n+1)
print(1000*F(7)/F(4))