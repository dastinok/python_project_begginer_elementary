hours_worked = int(input('Введите отработанные часы за неделю:  '))

hourly_labor_rate = int(input('Введите почасовую оплату труда: '))

HOURS_PER_WEEK = 40
RATIO = 1.5

if hours_worked > HOURS_PER_WEEK:
    print('Вы отработали больше! Вам положена надбавка!')
    overtime_hours = hours_worked - HOURS_PER_WEEK
    overtime_pay = overtime_hours * RATIO * hourly_labor_rate #  Получаем сверхурочные
    salary_per_week = HOURS_PER_WEEK * hourly_labor_rate + overtime_pay  # Зарплата с надбавкой
    print(f'Ваша зарплата составляет {salary_per_week} рублей')
else:
    print('Вы отработали стандартные часы!')
    salary_per_week = hours_worked * hourly_labor_rate  # Рассчет обычной зарплаты
    print(f'Ваша зарплата составляет {salary_per_week} рублей')
