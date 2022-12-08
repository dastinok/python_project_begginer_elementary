first = input('Будет ли на ужине вегетарианец? да/нет: ')
second = input('Будет ли на ужине веганец? да/нет: ')
third = input('Будет ли на ужине приверженец безглютеновой диеты? да/нет: ')

YES = 'да'
NO = 'нет'

if first == NO and second == NO and third == NO:
    print('Изысканные гамбургеры от Джо')
elif first == YES and second == NO and third == YES:
    print('Центральная пиццерия')
elif first == YES and second == YES and third == YES:
    print('Кафе за углом')
    print('Кухня шеф-повара')
elif first == YES and second == NO and third == NO:
    print('Блюда от итальянской мамы')

