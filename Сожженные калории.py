

CALO = 4.2
FIRST = 10
MAX = 31
COUNTER = 5

for counter in range(FIRST, MAX, COUNTER):
    calories = CALO * counter
    print(f'{calories: .2f} калории')