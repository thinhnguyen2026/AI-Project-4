import random

def read_tsp_file(filename):
    try:
        with open(filename) as f:
            n = int(f.readline())
            print(n)
            cities = [f.readline().strip() for _ in range(n)]
            for i in range(len(cities)):
                print(cities[i])
            cost_matrix = [[int(x) for x in f.readline().split()] for _ in range(n)]
            for row in cost_matrix:
                print(' '.join(map(str, row)))

            print("--------------------------")
            print("Now I will apply genetic algorithm in your file")
        return cities, cost_matrix
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the file name and try again.")
        exit()
        
def create_route(city_count):
    route = list(range(city_count))
    random.shuffle(route)
    return route

def initial_population(size, city_count):
    return [create_route(city_count) for _ in range(size)]

def calculate_cost(route, cost_matrix):
    total_cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
    total_cost += cost_matrix[route[-1]][route[0]]
    return total_cost

def tournament_selection(population, cost_matrix, tournament_size =3):
    tournament_size = min(tournament_size, len(population))
    tournament = random.sample(population, tournament_size)
    return min(tournament, key=lambda individual: calculate_cost(individual, cost_matrix))

def ordered_crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None]*len(parent1)
    child[start:end+1] = parent1[start:end+1]
    fill_values = [item for item in parent2 if item not in child]
    child = [item if item is not None else fill_values.pop(0) for item in child]
    return child

def mutate(route, mutation_rate=0.01):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            swap_with = random.randint(0, len(route)-1)
            route[i], route[swap_with] = route[swap_with], route[i]
    return route

def genetic_algorithm(filename, population_size=100, generations=50):
    cities, cost_matrix = read_tsp_file(filename)
    population = initial_population(population_size, len(cities))
    

    print("----------------")
    for generation in range(generations):
        new_population = []
        for _ in range(len(population) // 2):
            parent1 = tournament_selection(population, cost_matrix)
            parent2 = tournament_selection(population, cost_matrix)
            
            child1 = ordered_crossover(parent1, parent2)
            child2 = ordered_crossover(parent2, parent1)
            
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        population = new_population
        best_route = min(population, key=lambda r: calculate_cost(r, cost_matrix))
        print(f"Generation {generation}: Best cost = {calculate_cost(best_route, cost_matrix)}")

    best_route = min(population, key=lambda r: calculate_cost(r, cost_matrix))
    print("Best route:", ' -> '.join(cities[i] for i in best_route))
    print("Minimum cost:", calculate_cost(best_route, cost_matrix))

print("Welcome to TSP Program")
print("Now you can input your file name with the number of cities and the distance. Then, I will help you find the best path and resulting the best cost")
print("------------")
filename = input("Enter the path to your file: ")
print("This is your file format:")
genetic_algorithm(filename)