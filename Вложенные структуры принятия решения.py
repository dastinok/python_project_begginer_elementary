amount1 = int(input('Введите первое число: '))
amount2 = int(input('Введите второе число: '))

print(f'Вы ввели первое число - {amount1}')
print(f'Вы ввели второе число - {amount2}')

if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print(f'Первое число - {amount1}')
    else:
        print(f'Второе число - {amount2}')

if amount1 < 10 and amount2 > 100:
    print(f'Первое число - {amount1} и второе число - {amount2}')

if amount1 > 10 and amount2 > 100:
    print(f'Первое число - {amount1} и второе число - {amount2}')

if amount1 == amount2:
    print(f'Первое число - {amount1} и второе число - {amount2}')

