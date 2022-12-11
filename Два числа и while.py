
keep = 'Да'

while keep == 'Да':
    first = int(input('Введите первое число: '))
    second = int(input('Введите втоое число: '))
    print(f'Первое число = {first}\n'
          f'Второе число = {second}')
    add = first + second
    print(f'Результат = {add}')

    keep = input('Хотите еще снова? (Да/Нет): ')
