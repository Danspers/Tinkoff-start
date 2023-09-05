# чтение данных
n, m = map(int, input().split(' '))
denominations_str = input().split(' ')

# преобразование данных
denominations = [int(x) for x in denominations_str]
denominations.extend(denominations)
denominations = sorted(denominations, reverse=True)

# обработка данных
bag = []
for banknote in denominations:
    if n >= banknote:
        n -= banknote
        bag.append(banknote)

# вывод данных
if n == 0:
    print(len(bag))
    print(' '.join(map(str, bag)))
else:
    print(-1)