number_list = list(map(int, input().split(", ")))
even_index_list = []
for index in range(len(number_list)):
    if number_list[index] % 2 == 0:
        even_index_list.append(index)
print(even_index_list)