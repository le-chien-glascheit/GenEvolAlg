import random


def mu(N):
    return [random.randint(0, 32) for _ in range(N)]


def Ω(maxS, search_space, L, population):
    neighborhood = []
    for i in range(2 ** L):
        distance = 0
        for j in range(len(maxS)):
            if maxS[j] != search_space[i][j]:
                distance += 1
        if distance == 1:
            neighborhood.append((search_space[i], population[i]))
    return neighborhood


def create_si(L, N):
    xi = [format(x, 'b').zfill(L) for x in range(2 ** L)]
    search_space = []
    print('-' * 46 + '\n\n')

    population = mu(N)

    for i in range(N):
        max_code = random.choice(xi)
        search_space.append(max_code)
        si = int(max_code, 2)
        print(
            f'#{i + 1} Кодировка = {max_code}, Приспособленность = {population[i]}\n')
    print('\n\n' + '-' * 46 + '\n\n')

    return search_space, population


def breadth_search(L, N):
    search_space, population = create_si(L, N)

    maxS = random.choice(search_space)
    max_value = random.choice(population)

    i = 0
    while i < N:
        neighborhood = Ω(maxS, search_space, L, population)

        print(f"\n\nШаг {i + 1}:\n max = {max_value}, maxS = {maxS},"
              f"\nОкрестность({maxS}): {neighborhood}")

        if not neighborhood:
            break

        best_neighbor = max(neighborhood, key=lambda x: x[1], default=(None, max_value))

        if best_neighbor[1] > max_value:
            maxS = best_neighbor[0]
            max_value = best_neighbor[1]

            print("\033[031m" + f'\tВыбрано новое maxS = {maxS},'
                                f' новый max = {max_value}' + "\033[0m")
        else:
            break

        i += 1

    print(f"\n\t\tИскомое решение: maxS = {maxS},"
          f" его приспособленность max = {max_value}")


if __name__ == '__main__':
    L = 5
    N = 32

    breadth_search(L=L, N=N)
