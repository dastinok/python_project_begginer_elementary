

STOCKS_AMOUNT = 2000
PRICE_STOCK = 40
COMMISSION = 0.03
com_for_stocks = STOCKS_AMOUNT * PRICE_STOCK * COMMISSION
buy_amount = STOCKS_AMOUNT * PRICE_STOCK + com_for_stocks

print('Детали покупки:\n'
      f'Куплено акций {STOCKS_AMOUNT} штук, ' +
      f'по цене - {PRICE_STOCK} долларов за одну штуку. ' +
      f'Коммиссия уплачена в размере - {com_for_stocks: .2f} баксов ' +
      f'Потрачено на акции - {buy_amount} зеленых')

SELL_STOCK = 42.75
sell_stock_amount = STOCKS_AMOUNT * SELL_STOCK
com_for_sell = sell_stock_amount * COMMISSION
sell_amount = sell_stock_amount - com_for_sell


print('Две недели спустя:\n'
      f'Продано акций - {STOCKS_AMOUNT} штук, ' +
      f'по цене - {SELL_STOCK} долларов за штуку. ' +
      f'Коммиссия - {com_for_sell: .2f} баксов')

summ_amount = STOCKS_AMOUNT * PRICE_STOCK

balance_amount = (sell_stock_amount) - (buy_amount)



print(f'Информация:\n'
      f'Сумма уплаченная за акции: {buy_amount}. ' +
      f'Сумма проданных акций - {sell_stock_amount} баксов ' +
      f'Сумма остатка (прибыль/убыток) - {balance_amount} баксов))')