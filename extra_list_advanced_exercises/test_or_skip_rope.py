encrypted_message = input()

numbers_list = [int(char) for char in encrypted_message if char.isdigit()]
non_numbers_list = [char for char in encrypted_message if not char.isdigit()]

take_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 != 0]

result = []
index = 0

for i in range(len(take_list)):
    take = take_list[i]
    skip = skip_list[i]
    result.append("".join(non_numbers_list[index:index + take]))
    index += take + skip

print("".join(result))