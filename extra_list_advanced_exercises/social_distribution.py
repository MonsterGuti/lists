population_numbers = list(map(int, input().split(", ")))
wealth_minimum = int(input())

if sum(population_numbers) < len(population_numbers) * wealth_minimum:
    print("No equal distribution possible")
    exit()

for index in range(len(population_numbers)):
    if population_numbers[index] < wealth_minimum:
        needed = wealth_minimum - population_numbers[index]
        wealthiest_index = population_numbers.index(max(population_numbers))
        population_numbers[wealthiest_index] -= needed
        population_numbers[index] = wealth_minimum

print(population_numbers)
