numbers_string = input().split(" ")
count_of_removed_numbers = int(input())
list_of_integers = []
for num in numbers_string:
    list_of_integers.append(int(num))
for _ in range(count_of_removed_numbers):
    list_of_integers.remove(min(list_of_integers))
the_biggest_nums_string = ""
for index in range(len(list_of_integers)):
    the_biggest_nums_string += str(list_of_integers[index])
    if index != len(list_of_integers) - 1:
        the_biggest_nums_string += ", "
print(the_biggest_nums_string)
