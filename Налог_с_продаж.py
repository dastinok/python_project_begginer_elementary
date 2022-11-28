sum_purchase = float(input('Сумма покупки равна: '))
print(f'Вы купили товара на {sum_purchase} рублей')

FEDERAL_TAX = 0.05
REGION_TAX = 0.025

federal_tax_purchase = sum_purchase * FEDERAL_TAX
region_tax_purchase = sum_purchase * REGION_TAX

print(f'Федеральный нвлог с покупки = {federal_tax_purchase} рублей')
print(f'Региональный налог с покупки = {region_tax_purchase} рублей')

total_amount = sum_purchase + federal_tax_purchase + region_tax_purchase

print(f'Сумма покупки с налогами = {total_amount} рублей ')
