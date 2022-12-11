
total = 0

for x in range(1,31):
    total = (x/(31 - x))
    print(f'{total: .2f}')
print(f'Сумма = {sum(i/(31-i) for i in range(1,31))}')




