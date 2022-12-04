alph = 'абвгдеёжзиклмнопрстуфхцчшщыэюя'
alphsogl = 'бвгджзклмнпрстфхцчшщ'
c = 0
for x in alphsogl:
    for y in alph:
        for z in alph:
            for w in alph:
                t = x + y + z + w
                print(t)
                c += 1
print(c)