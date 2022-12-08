weight = float(input('Введите массу тела в кг: '))
height = float(input('Введите рост тела в м: '))
print('---------- Таблица данных ------------\n'
      f'1. Масса = {weight} кг\n'
      f'2. Рост = {height} м')

index_w_h = weight / (height ** 2)

print('---------- ИНДЕКС МАССЫ ТЕЛА ------------\n'
      f'ИМТ = {index_w_h: .2f}')

LOW_NORMA = 18.5
HIGH_NORMA = 25

if index_w_h < LOW_NORMA:
    print('ВАШ ВЕС! НИЖЕ НОРМЫ! ')
elif LOW_NORMA < index_w_h < HIGH_NORMA:
    print('ВАШ ВЕС ОПТИМАЛЬНЫЙ!')
else:
    print('ВАШ ВЕС БОЛЬШЕ НОРМЫ!')
