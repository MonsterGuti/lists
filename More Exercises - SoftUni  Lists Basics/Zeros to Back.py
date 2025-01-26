numbers = input().split(", ")
for i in range(len(numbers) - 1, -1, -1):
    numbers[i] = int(numbers[i])
for j in range(len(numbers) - 1, -1, -1):
    if numbers[j] == 0:
        numbers.remove(numbers[j])
        numbers.append(0)
print(numbers)
