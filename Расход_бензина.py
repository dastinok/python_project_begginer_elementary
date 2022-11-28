distance = float(input('Введите кол-во пройденных километров: '))
gasoline_consumption = float(input('Введите расход топлива в литрах: '))

your_consumption = distance / gasoline_consumption

print(f'Вы прошли {distance} километров\n',
      f'Вы потратил {gasoline_consumption} литров\n',
      f'Ваш расход бензина автомобилем состовляет {your_consumption}')
