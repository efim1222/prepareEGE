# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [11110; 55556],
# числа, имеющие ровно три различных натуральных делителя, не считая единицы и самого числа. Для каждого
# найденного числа запишите эти три делителя в таблицу на экране с новой строки.
for number in range(11110, 55557):
    count_delitel = 0
    delitelM = []
    for delitel in range(2, number):
        if number % delitel == 0:
            count_delitel += 1
            delitelM.append(delitel)
    if count_delitel == 3:
        print(delitelM)