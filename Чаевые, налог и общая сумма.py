food_price = float(input('Введите стоимость вашего блюда: '))
print(f'Стоимость вашего блюда составляет {food_price} рублей')

TIPS = 0.18
TAX = 0.07

get_tips = food_price * TIPS

print(f'Ваши чайвые составляют {get_tips} рублей')

get_tax = food_price * TAX

print(f'Ваш налог составляет {get_tax} рублей')

common_price = food_price + get_tips + get_tax

print((f'Итоговая сумма составляет {common_price} рублей'))
