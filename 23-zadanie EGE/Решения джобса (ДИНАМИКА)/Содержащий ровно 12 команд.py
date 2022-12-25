# +1
# *2 - 3
# Сколько различных результатов 
# можно получить из числа 3 после 
# выполнения программы, 
# содержащей ровно 12 команд?
s = {3}
for i in range(12):
    s = {x + 1  for x in s} | {x * 2 - 3 for x in s}
    
print(len(s))
# 377