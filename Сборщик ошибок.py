

print('---------Нарастающий итог кол-ва ошибок---------')

MAX = 5
error = 0

for collector in range(MAX):
    number = int(input('Введите кол-во ошибок: '))
    error = error + number

print(f'Общее кол-во ошибок = {error}')