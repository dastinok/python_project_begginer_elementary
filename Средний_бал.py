mark1 = int(input('Введите 1 оценку: '))
mark2 = int(input('Введите 2 оценку: '))
mark3 = int(input('Введите 3 оценку: '))

PASSING_SCORE = 90  # Магическое число
amount_tests = 3  # Количество тестов

average_mark = (mark1 + mark2 + mark3)/amount_tests  # Средний балл

print(f'Ваш средний бал равен {average_mark:.0f}')

if average_mark >= PASSING_SCORE:  # Условие
    print('Поздравляем, вы прошли тест!')  # Инструкция



