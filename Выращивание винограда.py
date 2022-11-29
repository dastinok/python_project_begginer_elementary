ridge_length = float(input('Введите длину гряды в метрах: '))
space_size = float(input('Введите размер пространства, занимаемых концевыми опорами в метрах: '))
distance = float(input('Введите расстояние между виноградными лозами в метрах: '))

number_of_vines = (ridge_length - 2*space_size) / distance

print(f'1. Длина гряды: {ridge_length} м \n'
      f'2. Размер пространства: {space_size} м \n'
      f'3. Расстояние: {distance} м \n'
      f'4. Количество виноградных лоз: {number_of_vines: .2f}')
