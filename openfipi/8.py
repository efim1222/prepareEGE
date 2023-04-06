from itertools import *
a = list(product("АЛПЦЯ", repeat=5))
c = 0
for i in a:
    b = ''.join(i)
    c += 1
    if b.count('А') <= 1 and b.count('Ц') == 2 and b.count('Л') == 0:
        print(b, c)