# чтение данных
input_string = input()

# подготовка данных
s = 0
h = 0
e = 0
r = 0
i = 0
f = 0

# подсчёт букв
for a in range(len(input_string)):
    if input_string[a] == 's':
        s += 1
    elif input_string[a] == 'h':
        h += 1
    elif input_string[a] == 'e':
        e += 1
    elif input_string[a] == 'r':
        r += 1
    elif input_string[a] == 'i':
        i += 1
    elif input_string[a] == 'f':
        f += 1

# постобработка данных
bag_of_letters = [s, h, e, r, i, f//2]

# вывод данных
print(min(bag_of_letters))