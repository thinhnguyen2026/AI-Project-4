def main():
    print("Welcome to TSP Program")
    print("Now you can input your file name with the number of cities and the distance. Then, I will help you find the best path and resulting the best cost")
    print("------------")

    file_name = input("Please enter a file name: ")

    try:
        with open(file_name, 'r') as file:
            n = int(file.readline().strip())

            cities = []
            for _ in range(n):
                city = file.readline().strip()
                cities.append(city)

            cost_grid = []
            for _ in range(n):
                costs = list(map(int, file.readline().strip().split()))
                cost_grid.append(costs)

            print(f"Number of cities: {n}")
            print("Cities:")
            for city in cities:
                print(city)
            print("Cost Grid:")
            for row in cost_grid:
                print(row)
                print("Good Bye")

    except FileNotFoundError:
        print("Error: The file doesn't exist. Please check the file and try again")
        exit()

if __name__ == "__main__":
    main()  