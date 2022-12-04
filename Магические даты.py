month = int(input('Введите месяц в числовой форме: '))
day = int(input('Введите день: '))
year = int(input('Введите двузначный год: '))

print(f'{day}.{month}.{year}')

magic_date = day * month

if magic_date == year:
    print('Введенная дата является МАГИЧЕСКОЙ!')
else:
    print('Дата не является магической!')