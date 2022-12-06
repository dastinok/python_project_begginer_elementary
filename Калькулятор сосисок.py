people = int(input('Введите кол-во участников пикника: '))
hot_dogs_amount = int(input('Введите кол-во хот-догов, для каждого участника: '))

PACKAGE_SASUGES = 10
PACKAGE_BUN = 8
PACKAGE = 1

hot_dogs = people * hot_dogs_amount
print(f'Кол-во хотдогов: {hot_dogs}')

if hot_dogs % PACKAGE_SASUGES != 0:
    min_package_sasuges = hot_dogs // PACKAGE_SASUGES + PACKAGE
    remains_of_sasuges = min_package_sasuges * 10 - hot_dogs
    print(f'Минимальное кол-во упаковок сосисек: {min_package_sasuges: .0f}')
    print(f'Остаток сосисек - {remains_of_sasuges: .0f} штук')
else:
    min_package_sasuges = hot_dogs // PACKAGE_SASUGES - PACKAGE
    remains_of_sasuges = min_package_sasuges * 10 - hot_dogs
    print(f'Минимальное кол-во упаковок сосисек: {min_package_sasuges: .0f}')
    print(f'Остаток сосисек - {remains_of_sasuges: .0f} штук')

if hot_dogs % PACKAGE_BUN != 0:
    min_package_bun = hot_dogs // PACKAGE_BUN + PACKAGE
    remains_of_bun = min_package_bun * 8 - hot_dogs
    print(f'Минимальное кол-во упаковок булочек: {min_package_bun: .0f}')
    print(f'Остаток булочек - {remains_of_bun: .0f} штук')

else:
    min_package_bun = hot_dogs // PACKAGE_BUN - PACKAGE
    remains_of_bun = min_package_bun * 8 - hot_dogs
    print(f'Минимальное кол-во упаковок булочек: {min_package_bun: .0f}')
    print(f'Остаток булочек - {remains_of_bun: .0f} штук')