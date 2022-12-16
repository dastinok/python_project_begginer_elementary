

STEP = -1
END_CYCLE = 0
MAX = 8

for count in range(MAX, END_CYCLE, STEP):
    for column in range(count-1):
        print('*', end='')
    print()