package = int(input('Введите кол-во купленных пакетов: '))
print(f'Вы приобрели {package} пакетов')

PACKAGE = 99
DISCOUNT_10 = 0.1
DISCOUNT_20 = 0.2
DISCOUNT_30 = 0.3
DISCOUNT_40 = 0.4


if 0 < package <= 9:
    print('Скидки нет!')
    final = package * PACKAGE
    print(f'Общая сумма покупки = {final} баксов')
elif 10 <= package <= 19:
    discount = package * DISCOUNT_10 * PACKAGE
    print(f'Ваша скидка = {discount} баксов')
    final = package * PACKAGE - discount
    print(f'Общая сумма покупки = {final} баксов')
elif 20 <= package <= 49:
    discount = package * DISCOUNT_20 * PACKAGE
    print(f'Ваша скидка = {discount} баксов')
    final = package * PACKAGE - discount
    print(f'Общая сумма покупки = {final} баксов')
elif 50 <= package <= 99:
    discount = package * DISCOUNT_30 * PACKAGE
    print(f'Ваша скидка = {discount} баксов')
    final = package * PACKAGE - discount
    print(f'Общая сумма покупки = {final} баксов')
else:
    discount = package * DISCOUNT_40 * PACKAGE
    print(f'Ваша скидка = {discount} баксов')
    final = package * PACKAGE - discount
    print(f'Общая сумма покупки = {final} баксов')

