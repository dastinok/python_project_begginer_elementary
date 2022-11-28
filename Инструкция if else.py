score = int(input('Введите ваш счет от 1 до 5: '))
print(f'Вы ввели {score}')

A_score = 5
B_score = 4
C_score = 3
D_score = 2
F_score = 1

if score >= A_score:
    print('Ваш уровень - А')
else:
    if score >= B_score:
        print('Ваш уровень B')
    else:
        if score >= C_score:
            print('Ваш уровень С')
        else:
            if score >= D_score:
                print('Ваш уровень D')
            else:
                print('Ваш уровень F')
