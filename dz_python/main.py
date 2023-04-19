n = int(input('Введите количество элементов в массиве -> '))
num_list = [i for i in range(1, n + 1)]
print(num_list)
x = int(input('Введите число Х -> '))
count = 0

for item in num_list:
    if item == x:
        count += 1

if count != 0: print(count, 'time(s)')
else:
    min_num = 0
    dif = 0
    min_dif = num_list[-1] # не уверен как задать переменную, 0 не вариант
    for item in num_list:
        dif = abs(item - x)
        if dif < min_dif:
            min_dif = dif
            min_num = item
    print(min_num)