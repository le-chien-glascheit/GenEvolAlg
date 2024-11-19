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
            print(f'Новый максимум приспособленности = {max},'
              f' кодировка = {maxS}')
        i += 1
print(f'Приспособленность = {maxS}, Кодировка = {max}')