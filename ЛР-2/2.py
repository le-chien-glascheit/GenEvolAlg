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
