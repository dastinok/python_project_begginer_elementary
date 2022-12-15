def convert():
    print('---------Вычисление Факториала числа--------')

    number = int(input('Введите неотрицательное целое число: '))

    print('Число\t\tФакториал')

    factorial = 1

    for count in range(number):
        count += 1
        factorial = count * factorial

        print(f'{count}\t\t\t\t{factorial}')

convert()
while True:
    flag = input('Ещё раз? [да/нет]: ')

    if flag == 'да':
        convert()
    else:
        break






