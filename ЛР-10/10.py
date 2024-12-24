import random

N = 15
max_weight = 80

# Данные по предметам: (номер, цена, вес)
items = [
    (1, 21, 2),
    (2, 19, 26),
    (3, 27, 23),
    (4, 3, 6),
    (5, 24, 19),
    (6, 30, 9),
    (7, 6, 8),
    (8, 13, 20),
    (9, 2, 11),
    (10, 21, 1),
    (11, 26, 17),
    (12, 26, 21),
    (13, 24, 7),
    (14, 1, 20),
    (15, 10, 11)
]


def randomInitialization():
    """Случайное формирование начальной популяции."""
    return [random.randint(0, 1) for _ in range(N)]


def greedyInitialization():
    """Жадное формирование начальной популяции."""
    solution = [0] * N
    total_weight = total_value = 0
    for i in range(N):
        if total_weight + items[i][2] <= max_weight:
            solution[i] = 1
            total_weight += items[i][2]
            total_value += items[i][1]
    return solution


def calcFitness(solution):
    """Функция для подсчета приспособленности."""
    total_value = sum(items[i][1] * solution[i] for i in range(N))
    total_weight = sum(items[i][2] * solution[i] for i in range(N))

    if total_weight > max_weight:
        return 0
    return total_value


def singlePointCrossover(parent1, parent2):
    """Одноточечное скрещивание."""
    point = random.randint(1, N - 1)
    child = parent1[:point] + parent2[point:]
    return child


def twoPointCrossover(parent1, parent2):
    """Двухточечное скрещивание."""
    point1 = random.randint(0, N - 1)
    point2 = random.randint(0, N - 1)

    if point1 > point2:
        point1, point2 = point2, point1

    child = parent1[:point1] + parent2[point1:point2] + parent1[point2:]

    return child


def simpleMutation(child):
    """Простая мутация."""
    mutation_rate = 0.1
    for i in range(N):
        if random.random() < mutation_rate:
            child[i] = 1 - child[i]
    return child


def replacementMutation(child):
    """Мутация с заменой."""
    mutation_rate = 0.1
    for i in range(N):
        if random.random() < mutation_rate:
            child[i] = random.randint(0, 1)  # Заменяем на случайное значение
    return child


def rouletteSelection(population):
    """Рулеточная селекция."""
    fitness_values = [calcFitness(ind) for ind in population]

    max_fitness = sum(fitness_values)

    if max_fitness == 0:
        return random.choice(population)

    pick = random.uniform(0, max_fitness)

    current = 0
    for ind in population:
        current += calcFitness(ind)
        if current > pick:
            return ind


def tournamentSelection(population):
    """Турнирная селекция."""
    tournament_size = min(3, len(population))

    tournament = random.sample(population, tournament_size)

    best_individual = max(tournament, key=calcFitness)

    return best_individual


def main():
    populations_number = int(input("Введите размер популяции: "))
    generations = int(input("Введите количество поколений: "))

    print("\tДоступные операторы формирования начальной популяции:")
    print("1 - Случайное формирование")
    print("2 - Жадное формирование")

    modeInit = int(input("Выберите оператор формирования начальной популяции (1-2): "))

    population = []

    for _ in range(populations_number):
        if modeInit == 1:
            population.append(randomInitialization())
        elif modeInit == 2:
            population.append(greedyInitialization())

    # Основной цикл генетического алгоритма


    for generation in range(generations):
        print(f"\nПоколение № {generation + 1}:")

        fitness_values = [calcFitness(ind) for ind in population]

        for i in range(populations_number):
            print(f"Индивид {i + 1}: {population[i]}, Приспособленность: {fitness_values[i]}")

        best_index = fitness_values.index(max(fitness_values))
        print("Лучшая особь:", population[best_index], f"| Приспособленность: {fitness_values[best_index]}")

        new_population = []

        while len(new_population) < populations_number:
            parent1 = rouletteSelection(population)  # Селектор может быть изменён на tournamentSelection
            parent2 = rouletteSelection(population)

            # Скрещивание
            if random.random() < 0.5:  # Шанс на одноточечное или двухточечное скрещивание
                child = singlePointCrossover(parent1, parent2)
            else:
                child = twoPointCrossover(parent1, parent2)

            # Мутация
            if random.random() < 0.5:  # Шанс на простую или замену мутации
                child = simpleMutation(child)
            else:
                child = replacementMutation(child)

            new_population.append(child)

        population = new_population

if __name__ == "__main__":
    main()
