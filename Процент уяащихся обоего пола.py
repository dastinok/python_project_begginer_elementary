men = int(input('Введите кол-во юношей: '))
girls = int(input('Введите кол0во девушек: '))

print(f'Юношей - {men}')
print(f'Девушек - {girls}')

all_amount = men + girls

print(f'Общее кол-во = {all_amount}')

procent_men = men / all_amount * 100

print(f'Кол-во юношей - {procent_men: .0f}%')

procent_girls = girls / all_amount * 100

print(f'Кол-во девушек - {procent_girls: .0f}%')

