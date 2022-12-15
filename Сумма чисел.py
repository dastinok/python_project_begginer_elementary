print('----------Сумма чисел------------')

amount = 0
numbers = 0

while numbers >= 0:
    numbers = int(input('Введите число положительное: '))
    print(numbers)

    amount = amount + numbers

    if numbers < 0:
        amount = amount - numbers
        print('Вы ввели отрицательное число. Финиш')
        print(f'Сумма положительных чисел =  {amount}')




