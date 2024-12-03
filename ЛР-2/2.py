import random

L = 5
N = 10


def mu(x, L):
    return (x - 2 ** (L - 1)) ** 2


#  𝛀(𝒎𝒂𝒙𝑺)
def 𝛀(maxS, search_space, L):
    neighborhood = []
    for i in range(2 ** L):
        distance = 0
        for j in range(len(maxS)):
            if maxS[j] != search_space[i][j]:
                distance += 1
        if distance == 1:
            neighborhood.append((format(i, 'b').zfill(L), mu(i, L)))
    return neighborhood


def create_si(L, N):
    xi = [format(x, 'b').zfill(L) for x in range(2 ** L)]
    search_space = []
    print('-' * 46 + '\n\n')
    for i in range(N):
        max = random.choice(xi)
        search_space.append(max)
        si = int(max, 2)
        print(f'#{i + 1}  Кодировка = {max}, приспособленность = {si}\n')
    print('\n\n' + '-' * 46 + '\n\n')
    return search_space


def depth_search(L, N):
    search_space = create_si(L, N)
    maxS = random.choice(search_space)
    max = mu(int(maxS, 2), L)
    neighborhood = 𝛀(maxS, search_space, L)

    for i in range(N):
        print(f"\n\nШаг {i + 1}:\n max = {max}, maxS = {maxS},"
              f"\nОкрестность({maxS}): {neighborhood}")

        if not neighborhood:
            break

        si = random.choice(neighborhood)
        print(f'Смотрим на случайный si из 𝛀(maxS): {si}')
        neighborhood.remove(si)

        if max < mu(int(si[0], 2), L):
            maxS = si[0]
            max = mu(int(maxS, 2), L)

            neighborhood = 𝛀(maxS, search_space, L)
            print("\033[031m" + f'\tВыбрано новое maxS = {maxS},'
                                f' новый max = {max}' + "\033[0m")

    print(f"\n\t\tИскомое решение: maxS = {maxS},"
          f" его приспособленность max = {max}")


if __name__ == '__main__':
    L = 5
    N = 32

    depth_search(L=L, N=N)
