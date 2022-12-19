# Ксюша составляет слова, меняя местами буквы в слове МИМИКРИЯ. Сколько различных слов, включая исходное, может составить Ксюша?
from itertools import * 
a = list(permutations('МИМИКРИЯ'))
c = set()
for x in a:
    b = ''.join(x)
    c.add(b)
    
print(len(c))