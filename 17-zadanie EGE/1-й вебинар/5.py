# 235)	В файле 17-1.txt содержится последовательность целых чисел. 
# Элементы последовательности могут принимать целые значения от 
# –10 000 до 10 000 включительно. Определите количество троек, 
# в которых хотя бы два из трёх элементов больше, чем среднее арифметическое всех чисел в файле. 
# В ответе запишите два числа: сначала количество найденных троек,
# а затем – максимальную сумму элементов таких троек. 
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
with open('17-1.txt') as a:
    s = [int(x) for x in a]
    srarph = sum(s) / len(s)
    res = []
    for x in range(len(s) - 2):
        if (s[x] > srarph and s[x + 1] > srarph) or (s[x] > srarph and s[x + 2] > srarph)\
            or (s[x + 1] > srarph and s[x + 2] > srarph):
                res.append(s[x] + s[x + 1] + s[x + 2])
    print(len(res), max(res))