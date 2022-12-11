another = 'Да'

while another == 'Да':
    number = int(input('Введите значение от 0 до 100: '))
    print(f'Вы ввели {number}')

    while 0 > number or number > 100:
        print('Ошибка! Введите в пределах нормы!')
        number = int(input('Введите значение от 0 до 100: '))
    another = input('Продолжить (Да/Нет): ')