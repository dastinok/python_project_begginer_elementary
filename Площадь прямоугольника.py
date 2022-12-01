
length1 = float(input('Введите длину прямоугольника в см: '))
width1 = float(input('Введите ширину прямоугольника в см: '))

length2 = float(input('Введите длину прямоугольника в см: '))
width2 = float(input('Введите ширину прямоугольника в см: '))

rectangle_area_1 = length1 * width1
rectangle_area_2 = length2 * width2

print(f'1. Площаль первого прямоугольника = {rectangle_area_1: .2f}\n'
      f'2. Площадь второго прямоугольника = {rectangle_area_2: .2f}')

if rectangle_area_1 > rectangle_area_2:
    print('Первый прямоугольник больше')
elif rectangle_area_1 < rectangle_area_2:
    print('Второй прямоугольник больше')
else:
    print('Прямоугольники равны')

