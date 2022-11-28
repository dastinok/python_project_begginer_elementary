price_product1 = float(input('Введите цену 1 товара:'))
price_product2 = float(input('Введите цену 2 товара: '))
price_product3 = float(input('Введите цену 3 товара: '))
price_product4 = float(input('Введите цену 4 товара: '))
price_product5 = float(input('Введите цену 5 товара: '))

SALES_TAX = 0.1

all_price = price_product1 + price_product2 + price_product3 + price_product4 + price_product5


print(f'Общая стоимость товаров = {all_price:.2f} рублей')

tax_product1 = price_product1 * SALES_TAX
tax_product2 = price_product2 * SALES_TAX
tax_product3 = price_product3 * SALES_TAX
tax_product4 = price_product4 * SALES_TAX
tax_product5 = price_product5 * SALES_TAX

sum_tax_product = tax_product1 + tax_product2 + tax_product3 + \
                  tax_product4 + tax_product5

print(f'Сумма налога с продаж составляет {sum_tax_product:.2f} рублей')

total_amount = all_price + sum_tax_product

print(f'Общая сумма = {total_amount:.2f} рублей')



