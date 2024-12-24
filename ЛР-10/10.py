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


def unitInitialization():
    return [random.randint(0, 1) for _ in range(N)]


def calcFitness(solution):
    total_value = sum(items[i][1] * solution[i] for i in range(N))
    total_weight = sum(items[i][2] * solution[i] for i in range(N))

    if total_weight > max_weight:
        return 0
    return total_value


def crossover(parent1, parent2):
    point = random.randint(1, N - 1)
    child = parent1[:point] + parent2[point:]
    return child


def mutate(child):
    mutation_rate = 0.1
    for i in range(N):
        if random.random() < mutation_rate:
            child[i] = 1 - child[i]
    return child


def main():
    populations_number = int(input("Введите размер популяции: "))
    generations = int(input("Введите количество поколений: "))

    population = [unitInitialization() for _ in range(populations_number)]

    for generation in range(generations):
        print(f"\nПоколение № {generation + 1}:")

        mu = [calcFitness(ind) for ind in population]

        for i in range(populations_number):
            print(f"Индивид {i + 1}: {population[i]}, Приспособленность = {mu[i]}")

        best_index = mu.index(max(mu))
        print("Лучшая особь:", population[best_index], f" | Приспособленность = {mu[best_index]}")

        new_population = []

        while len(new_population) < populations_number:
            parents_indices = random.sample(range(populations_number), k=2)
            parent1 = population[parents_indices[0]]
            parent2 = population[parents_indices[1]]

            child = crossover(parent1, parent2)
            child = mutate(child)

            new_population.append(child)

        population = new_population


if __name__ == "__main__":
    main()
