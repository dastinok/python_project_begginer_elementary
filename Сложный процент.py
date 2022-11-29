principal_amount = float(input('Введите основную сумму в рублях: '))
annual_interest_rate = float(input('Введите годовую процентную ставку в процентах: '))

ANNUAL_INTEREST_RATE = annual_interest_rate / 100

interest_income = float(input('Введите частоту процентного дохода в год: '))

time = float(input('Конкретное количество лет: '))

money_on_account = principal_amount * (1 + (ANNUAL_INTEREST_RATE / interest_income)) ** (interest_income * time)

print(f'1. Основная сумма: {principal_amount} рублей \n'
      f'2. Годовая процентная ставка: {annual_interest_rate}% \n'
      f'3. Частота процентного дохода: {interest_income} \n'
      f'4. Количество лет: {time} \n'
      f'5. Денежная сумма на счете: {money_on_account: .2f} рублей')