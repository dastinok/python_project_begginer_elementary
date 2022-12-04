weight = int(input('Введите массу тела в кг: '))
print(f'Вы ввели {weight} килограмм')

CONSTANT = 9.8
HEAVY_BODY = 500
LIGHT_BODY = 100

wt = weight * CONSTANT

print(f'Вес = {wt: .2f} Ньютон')

if wt > HEAVY_BODY:
    print('Тело слишком тяжелое')
elif wt < LIGHT_BODY:
    print('Тело слишком легкое')
else:
    print('Тело среднее')
