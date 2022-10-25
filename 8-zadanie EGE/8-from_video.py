#Cколько существует шестизначных чисел, делящихся на пять, в которых каждая цифра повторяется ровно один раз,
#при этом никакие две четные и две нечетные не стоят рядом
import itertools

a = list(itertools.permutations('0123456789', r=6))
forbiddens = list(itertools.permutations('13579', r=2)) + list(itertools.permutations('02468', r=2))
count = 0
for x in a:
    s = ''.join(x)
    if s[0] != '0' and (s[-1] == '0' or s[-1] == '5'):
        for forbidden in forbiddens:
            s1 = ''.join(forbidden)
            if s1 in s:
                break
        else:
            count+=1
            print(s)
print(count)
