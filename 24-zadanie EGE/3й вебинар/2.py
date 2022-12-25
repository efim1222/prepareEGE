# 224)	Текстовый файл 24-224.txt содержит строку из символов A, B и C, 
# всего не более чем 106 символов. 
# Найдите максимальную длину строки, состоящей только из комбинаций BAC и СAB. 
# Например, в строке BABABACCABCABCB такая подстрока BACCABCAB (длина 9).
f = open('24-224.txt')
s = f.readline()
s = s.replace('BACAB', 'BAC CAB').replace('CABAC', 'CAB BAC')
s = s.replace('BAC', '***').replace('CAB', '***')
t = ''
while t in s:
    t += '*'
print(len(t) - 1) 
# 72