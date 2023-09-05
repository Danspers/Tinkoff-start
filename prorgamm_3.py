# чтение данных
n = int(input())
joe_str = input().split(' ')
win_str = input().split(' ')

# преобразование данных
joe = [int(x) for x in joe_str]
win = [int(x) for x in win_str]

# поиск отрезка
indexs = []
for i in range(n):
    if joe[i] != win[i]:
        indexs.append(i)

begin = indexs[0]
end = indexs[-1] 

joe[begin : end+1] = sorted(joe[begin : end+1])

# вывод данных
if joe == win:
    print('YES')
else:
    print('NO')