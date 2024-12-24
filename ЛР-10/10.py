import random

N = 15
max_weight = 80

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
    return [random.randint(0, 1) for _ in range(N)]


def greedyInitialization():
    solution = [0] * N
    total_weight = total_value = 0
    for i in range(N):
        if total_weight + items[i][2] <= max_weight:
            solution[i] = 1
            total_weight += items[i][2]
            total_value += items[i][1]
    return solution


def calcFitness(solution):
    total_value = sum(items[i][1] * solution[i] for i in range(N))
    total_weight = sum(items[i][2] * solution[i] for i in range(N))

    if total_weight > max_weight:
        return 0, total_weight
    return total_value, total_weight


def singlePointCrossover(parent1, parent2):
    point = random.randint(1, N - 1)
    child = parent1[:point] + parent2[point:]
    return child


def twoPointCrossover(parent1, parent2):
    point1 = random.randint(0, N - 1)
    point2 = random.randint(0, N - 1)

    if point1 > point2:
        point1, point2 = point2, point1

    child = parent1[:point1] + parent2[point1:point2] + parent1[point2:]

    return child


def simpleMutation(child):
    mutation_rate = 0.1
    for i in range(N):
        if random.random() < mutation_rate:
            child[i] = 1 - child[i]
    return child


def replacementMutation(child):
    mutation_rate = 0.1
    for i in range(N):
        if random.random() < mutation_rate:
            child[i] = random.randint(0, 1)
    return child


def rouletteSelection(population):
    fitness_values = [calcFitness(ind)[0] for ind in population]

    max_fitness = sum(fitness_values)

    if max_fitness == 0:
        return random.choice(population)

    pick = random.uniform(0, max_fitness)

    current = 0
    for ind in population:
        current += calcFitness(ind)[0]
        if current > pick:
            return ind


def tournamentSelection(population):
    tournament_size = min(3, len(population))

    tournament = random.sample(population, tournament_size)

    best_individual = max(tournament, key=lambda ind: calcFitness(ind)[0])

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

    for generation in range(generations):
        print(f"\nПоколение № {generation + 1}:")

        fitness_values = [calcFitness(ind) for ind in population]

        for i in range(populations_number):
            value_fit, weight_fit = fitness_values[i]
            print(f"Индивид {i + 1}: {population[i]}, Приспособленность: {value_fit}, Вес: {weight_fit}")

        best_index = fitness_values.index(max(fitness_values))
        best_value_fit, best_weight_fit = fitness_values[best_index]
        print("Лучшая особь:", population[best_index], f"| Приспособленность: {best_value_fit}, Вес: {best_weight_fit}")

        new_population = []

        while len(new_population) < populations_number:
            parent1 = rouletteSelection(population)
            parent2 = rouletteSelection(population)

            if random.random() < 0.5:
                child = singlePointCrossover(parent1, parent2)
            else:
                child = twoPointCrossover(parent1, parent2)

            if random.random() < 0.5:
                child = simpleMutation(child)
            else:
                child = replacementMutation(child)

            new_population.append(child)

        population = new_population


if __name__ == "__main__":
    main()
