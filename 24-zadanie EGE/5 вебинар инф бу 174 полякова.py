# 176)Текстовый файл 24-157.txt содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых нет сочетания символов  QW.
with open('24-157.txt') as a:
    list_of_all_letters = list(str(x) for x in a)
    string_of_all_letters = ''.join(list_of_all_letters)
    divide_for_Q_W = string_of_all_letters.replace('QW', 'Q W')
    divide_by_space = divide_for_Q_W.split()
    lengths_of_elements_without_QW = []
    for len_divide_by_space in divide_by_space:
        lengths_of_elements_without_QW.append(len(len_divide_by_space))
    print(max(lengths_of_elements_without_QW))
    print(max(list(map(len, divide_by_space))))
