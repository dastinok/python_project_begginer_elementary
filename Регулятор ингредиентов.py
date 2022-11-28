bun_amount = float(input('Введите кол-во булочек: '))

print(f'Вы запрсили {bun_amount} булочек')

glass_of_sugar = 0.03125
glass_of_butter = 0.02083
glass_of_flour = 0.05729

sugar_amount = glass_of_sugar * bun_amount
print(f'Количество стаканов сахара: {sugar_amount: .2f}')

butter_amount = glass_of_butter * bun_amount
print(f'Количество стаканов масла: {butter_amount: .2f}')

flour_amount = glass_of_flour * bun_amount
print(f'Количество стаканов муки: {flour_amount: .2f}')





