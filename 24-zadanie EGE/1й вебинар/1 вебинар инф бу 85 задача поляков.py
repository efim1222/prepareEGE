# 85)	Текстовый файл k8-9.txt состоит не более чем из 10**6 символов.
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
with open('k8-9.txt') as a:
    s = list(str(x) for x in a)
    b = ''.join(s)
    l = lmax = 1
    for i in range(len(b)-1):
        if b[i] != b[i+1]:
            l += 1
            lmax = max(l, lmax)
        else:
            l = 1
    print(lmax)