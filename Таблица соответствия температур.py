

START_TEMPERATURE = -1
END_TEMPERATURE = 20
STEP = 1

K1 = 9 / 5
K2 = 32


print(f'Градусы Цельсия\t\t  Фаренгейт')

for celsius in range(START_TEMPERATURE, END_TEMPERATURE, STEP):
    celsius += 1
    F = K1 * celsius + K2
    print(f'\t{celsius: .1f}\t\t\t\t{F: .1f}')
