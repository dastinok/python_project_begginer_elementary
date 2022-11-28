# Типы данных и переменная
# int, float, boolean, str, list, None
value = None
a = 123
b = 1.23
print(type(a))
print(type(b))
value = 12334
print(type(value))

s = "hello world"
print(s) # вывод строки

d = 'hello \'word'
print(d)

z = 'hello \nword'
print(z)

print(a, b, s, d, z)
print(a, '-', b, '-', d)
print('{} - {} - {}'.format(a, b, s, d, z))
print(f'{a} - {b} - {s}')
print('{1} - {3} - {2}'.format(a, b, s, d, z))

f = True # Или False
print(f)

list = [1,2,3]
print(list)

g = ["dsfd", "орвпуар", "736276"]
print(g)