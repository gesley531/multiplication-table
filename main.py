# Times Tables v2
from time import sleep
num = int(input('\nEnter a number and I show the times tables: '))

for c in range(1, 101):
    print(f'\n{num} X {c} = {num * c}')
    sleep(1)