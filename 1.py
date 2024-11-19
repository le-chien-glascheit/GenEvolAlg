import random

i = 0
L = 15
N = L
max = 0
maxS = ''
si = ''

while i < N:
        si = ''.join(random.choice('01') for _ in range(L))
        print(f'Шаг {i+1}: si = {si}')
        if int(si, 2) > max:
            max = int(si, 2)
            maxS = si
            print(f"\033[031m" + 'Новый максимум приспособленности = {max}' + "\033[0m")

        print(f'\tТекущий максимум приспособленности = {max}')
        print(f'\tКодировка = {maxS}')
        print(f'\tВыбираемая кодировка на текущем шаге: = {si}')
        print(f"\tПриспособленность выбираемой кодировки = {int(si, 2)} ")
        print('\n\r')

        i += 1
print(f'Приспособленность = {max}, Кодировка = {maxS}')