numbers = input().split()
k = int(input())
step = k - 1
new_numbers_list = []
index = step

while numbers:
    if index >= len(numbers):
        index %= len(numbers)

    new_numbers_list.append(int(numbers[index]))
    numbers.pop(index)
    index += step

final_output = "["
for i in range(len(new_numbers_list)):
    final_output += str(new_numbers_list[i])
    if i != len(new_numbers_list) - 1:
        final_output += ","
final_output += "]"

print(final_output)
