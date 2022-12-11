

MAX = 10

total = 0
amount = int(input('Введите общую сумму в рублях: '))
print(f'{amount}')

for count in range(MAX):
    first = int(input('Статья расхода в рублях: '))
    print(f'{first}')
    total = total + first


print(f'Общая сумма - {total} рублей')

compare = amount - total
print(f'Прибыль или убыток: {compare} рублей')


