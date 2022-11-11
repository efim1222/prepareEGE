import itertools
a = list(itertools.product('СРГЕЙ', repeat=5))
c = 0
for x in a:
    b = ''.join(x)
    if b.count('Й') <= 1 and b[0] != 'Й' and b[4] != 'Й' and (not 'ЕЙ' in b) and (not 'ЙЕ' in b):
        print(b)
        c += 1
print(c)