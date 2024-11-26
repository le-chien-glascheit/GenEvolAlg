import random

def fitness_func(x):
    # Выберите один из вариантов для приспособленности
    # a. приспособленность соответствует натуральному значению бинарного кода
    # return x
    # b. приспособленность вычисляется как квадратичная функция
    return (x - 2**(5-1))**2
    # c. случайное задание приспособленностей
    # return random.randint(0, 10) # пример случайной приспособленности

def hill_climbing_search(L, N):
    i = 0
    maxS = random.randint(0, 2**L-1) # случайный выбор начальной кодировки
    max_fitness = fitness_func(maxS)
    
    while i < N:
        print(f"Шаг {i}:")
        print(f"Текущий maxS: {maxS}")
        print(f"Текущая приспособленность max: {max_fitness}")
        
        omega_maxS = []
        for j in range(-1, 2): # окрестность maxS
            neighbor = maxS ^ (1 << j)
            if 0 <= neighbor < 2**L:
                omega_maxS.append(neighbor)
        
        if len(omega_maxS) > 0:
            si = random.choice(omega_maxS)
            print(f"Выбранное si: {si}")
            omega_maxS.remove(si)
            
            if fitness_func(si) > max_fitness:
                maxS = si
                max_fitness = fitness_func(si)
                print("Произошла смена max и maxS")
        else:
            print("Не удалось найти лучшего соседа")
            break
        
        i += 1
    
    print("\nИскомое решение:")
    print(f"maxS: {maxS}")
    print(f"Приспособленность max: {max_fitness}")

# Пример использования
L = 5
N = 10
hill_climbing_search(L, N)

import random

L = 5
N = 10

# Функция для вычисления приспособленности второго варианта
def fitness(x):
    return (x - 2**(L-1))**2

# Функция для создания окрестности 𝛀(𝒎𝒂𝒙𝑺)
def create_neighborhood(maxS):
    neighborhood = []
    for i in range(2**L):
        neighborhood.append((i, fitness(i)))
    return neighborhood

# Функция для выполнения метода поиска в глубину
def depth_search():
    i = 0
    maxS = random.randint(0, 2**L-1)
    max_val = fitness(maxS)
    neighborhood = create_neighborhood(maxS)

    while i < N:
        print(f"Шаг {i+1}: max = {max_val}, maxS = {maxS}, Окрестность({maxS}): {neighborhood}")

        if not neighborhood:
            break

        si = random.choice(neighborhood)
        neighborhood.remove(si)

        if fitness(si[0]) > max_val:
            maxS = si[0]
            max_val = si[1]
            neighborhood = create_neighborhood(maxS)
            print(f"   Выбрано новое maxS = {maxS}, новый max = {max_val}")

        i += 1

    print(f"Искомое решение: maxS = {maxS}, его приспособленность max = {max_val}")

# Запуск метода поиска в глубину
depth_search()

