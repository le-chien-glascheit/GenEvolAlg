import random

L = 5
N = 10


def xi(x):
    return (x - 2 ** (L - 1)) ** 2


#  𝛀(𝒎𝒂𝒙𝑺)
def create_neighborhood(maxS):
    neighborhood = []
    for i in range(2 ** L):
        neighborhood.append((i, xi(i)))
    return neighborhood


def depth_search(L, N):
    i = 0
    maxS = random.randint(0, 2 ** L - 1)
    max_val = xi(maxS)
    neighborhood = create_neighborhood(maxS)

    while i < N:
        print(f"\n\nШаг {i + 1}:\n max = {max_val}, maxS = {maxS},"
              f"\nОкрестность({maxS}): {neighborhood}")

        if not neighborhood:
            break

        si = random.choice(neighborhood)
        neighborhood.remove(si)

        if xi(si[0]) > max_val:
            maxS = si[0]
            max_val = si[1]
            neighborhood = create_neighborhood(maxS)
            print("\033[031m" + f'\tВыбрано новое maxS = {maxS},'
                                f' новый max = {max_val}' + "\033[0m")

        i += 1

    print(f"\n\t\tИскомое решение: maxS = {maxS},"
          f" его приспособленность max = {max_val}")


if __name__ == '__main__':
    L = 5
    N = 10

    depth_search(L=L, N=N)
