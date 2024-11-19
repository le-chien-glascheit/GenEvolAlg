import random

def monte_carlo(maxS,L,N):
    i = 0
    max = 0
    while i < N:
            si = ''.join(random.choice(L))
            print(f'Шаг {i+1}: si = {si}')
            if int(si, 2) > max:
                max = int(si, 2)
                maxS = si
                print("\033[031m" + f'Новый максимум приспособленности = {max}' + "\033[0m")

            print(f'\tТекущий максимум приспособленности = {max}')
            print(f'\tКодировка = {maxS}')
            print(f'\tВыбираемая кодировка на текущем шаге: = {si}')
            print(f"\tПриспособленность выбираемой кодировки = {int(si, 2)} ")
            print('\n\r')

            i += 1
    print(f'Приспособленность = {max}, Кодировка = {maxS}')

if __name__ == '__main__':
    # i = 0
    # max = 0
    L = 15
    N = 32
    maxS = ''
    xi = [format(x, 'b').zfill(L) for x in range(2 ** L)]
    monte_carlo(maxS=maxS,L=xi,N=N)