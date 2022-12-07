number_5 = int(input('Введите кол-во монет достоинством 5 копеек: '))
number_10 = int(input('Введите кол-во монет достоинством 10 копеек: '))
number_50 = int(input('Введите кол-во монет достоинством 50 копеек: '))

print(f'Вы ввели {number_5} монет по 5 копеек\n'
      f'Вы ввели {number_10} монет по 10 копеек\n'
      f'Вы ввели {number_50} монет по 50 копеек')

PENNY_5 = 5
PENNY_10 = 10
PENNY_50 = 50
ROUBLE = 1

penny_amount_5 = number_5 * PENNY_5
penny_amount_10 = number_10 * PENNY_10
penny_amount_50 = number_50 * PENNY_50

print(f'Количество денег:\n'
      f'1. {penny_amount_5} копеек\n'
      f'2. {penny_amount_10} копеек\n'
      f'3. {penny_amount_50} копеек')

final = penny_amount_5 + penny_amount_10 + penny_amount_50
print(f'Итоговое значение = {final} копеек')

final_roubles = final / 100
print(f'Итоговое значение = {final_roubles} рублей')


if final_roubles == ROUBLE:
      print('Вы ВЫЙГРАЛИ! ПОЗДРАВЛЯЕМ!')
elif final_roubles > ROUBLE:
      print('Вы ввели значение больше. Попробуйте еще раз')
else:
      print('Вы ввели значение меньше. Попробуйте еще раз')







