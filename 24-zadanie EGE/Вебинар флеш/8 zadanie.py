# Текстовый Файл состопт не более чем пз 120000 спмволов P. Q. S. п R.
# Определите максимальное количество идущих подряд символов, среди которых нет R, стоящих рядом.
# Для выполнения этого задания следует написать программу.
s = open('24_8.txt').readline()
s = s.replace('RR', 'R*R')
s = s.replace('RR', 'R*R')
s = s.split('*')
print(len(max(s, key=len)))