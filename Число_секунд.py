#Задача 9
#Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

numbers = int(input("Введите кол-во секунд: "))
days = numbers // 86400  # Находим кол-во целых дней
numbers = numbers % 86400  # Находим остаток секунд

hours = numbers // 3600
numbers = numbers % 3600

minute = numbers // 60
numbers = numbers % 60

print(f'{days}:{hours}:{minute}:{numbers}')




