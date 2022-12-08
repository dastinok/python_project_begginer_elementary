seconds = int(input('Введите кол-во секунд: '))
print(f'Вы ввели {seconds} секунд')

MINUTE = 60
HOUR = 3600
DAY = 86400

if MINUTE <= seconds < HOUR:
    minute = seconds // MINUTE
    second = seconds % MINUTE
    print('----------ТАБЛИЦА ПРЕОБРАЗОВАНИЯ-----------\n'
          f'{minute} минута\n'
          f'{second} секунд')
elif HOUR <= seconds < DAY:
    hour = seconds // HOUR
    minutes = (seconds // MINUTE) % MINUTE
    second = seconds % MINUTE
    print('----------ТАБЛИЦА ПРЕОБРАЗОВАНИЯ-----------\n'
          f'{hour} часы\n'
          f'{minutes} минута\n'
          f'{second} секунд')
else:
    day = seconds // DAY
    hour = (seconds - DAY) // HOUR
    minutes = (seconds // MINUTE) % MINUTE
    second = seconds % MINUTE
    print('----------ТАБЛИЦА ПРЕОБРАЗОВАНИЯ-----------\n'
          f'{day} день\n'
          f'{hour:.0f} час(ы)\n'
          f'{minutes} минута\n'
          f'{second} секунд')
