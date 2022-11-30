def convert():
    MAX_TEMP = 103.56
    temperature = float(input('Введите температуру в Цельсиях: '))
    print(f'Вы ввели {temperature}С\N{DEGREE SIGN}')


    while temperature > MAX_TEMP:
        print('Убавь температуру! Подожди 5 минут и повтори процесс')
        temperature = float(input('Введите температуру в Цельсиях: '))

    print('Температура приемлемая. Проверьте через 15 минут.')

convert()
while True:
    flag = input('Ещё раз? [да/нет]: ')

    if flag == 'да':
        convert()
    else:
        break













