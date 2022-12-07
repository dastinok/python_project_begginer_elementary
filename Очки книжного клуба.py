books = int(input('Введите кол-во книг купленных в этом месяце: '))
print(f'Вы купили {books} книг')

if 0 <= books <= 1:
    print('Вы набрали НОЛЬ очков!')
elif 2<= books <= 3:
    print('Вы набрали 5 очков')
elif books == 4 or books == 5:
    print('Вы набрали 15 очков')
elif books == 6 or books == 7:
    print('Вы набрали 30 очков')
else:
    print('У вас 60 ОЧКО. Потресающе!')