import sys
sys.setrecursionlimit(10000)

def f(n):
    if n ** 0.5 == int(n ** 0.5):
        return n ** 0.5
    if n ** 0.5 != int(n ** 0.5):
        return f(n + 1) + 1
print(f(4850) + f(5000))
