# чтение данных
n, s = map(int, input().split(' '))
guns_str = input().split(' ')

# преобразование данных
guns = [int(x) for x in guns_str]

# обработка данных
max_gun = 0
for gun in guns:
    if (gun > max_gun) and (gun <= s):
        max_gun = gun

# вывод данных
print(max_gun)