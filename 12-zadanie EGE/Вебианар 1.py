# 118)	Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки цифр.
# заменить (v, w)
# нашлось (v)
# Дана программа для исполнителя Редактор:
# НАЧАЛО
# ПОКА нашлось (222) ИЛИ нашлось (888)
#   ЕСЛИ нашлось (222)
    # ТО заменить (222, 8)
    # ИНАЧЕ заменить (888, 2)
#   КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ
# Какая строка получится в результате применения приведённой выше программы к строке, состоящей из 93 идущих подряд цифр 8? В ответе запишите полученную строку.
# 
# 


s = '8' * 93
while '222' in s or '888' in s:
    if '222' in s:
        s = s.replace('222', '8', 1)
    else:
        s = s.replace('888', '2', 1)
print(s)
