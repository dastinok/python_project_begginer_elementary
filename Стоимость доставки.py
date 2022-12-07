weight = float(input('Введите массу пакета в граммах: '))
print(f'Масса пакета состовляет {weight} гр')


PAYMENT_1 = 150
PAYMENT_2 = 300
PAYMENT_3 = 400
PAYMENT_4 = 475
RATIO = 100


if weight <= 200:
    final = PAYMENT_1 * weight / RATIO
    print(f'Плата за доставку = {final} рубликов')
elif 201<= weight <= 600:
    final = PAYMENT_2 * weight / RATIO
    print(f'Плата за доставку = {final} рубликов')
elif 601 <= weight <= 1000:
    final = PAYMENT_3 * weight / RATIO
    print(f'Плата за доставку = {final} рубликов')
else:
    final = PAYMENT_4 * weight / RATIO
    print(f'Плата за доставку = {final} рубликов')