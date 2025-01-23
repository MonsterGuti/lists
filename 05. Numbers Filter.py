n = int(input())
list_of_numbers = []
for i in range(n):
    num = int(input())
    list_of_numbers.append(num)
filtered_list_of_numbers = []
command = input()
if command == "even":
    for number in list_of_numbers:
        if number % 2 == 0:
            filtered_list_of_numbers.append(number)
elif command == "odd":
    for number in list_of_numbers:
        if number %2 != 0:
            filtered_list_of_numbers.append(number)
elif command == "negative":
    for number in list_of_numbers:
        if number < 0:
            filtered_list_of_numbers.append(number)
elif command == "positive":
    for number in list_of_numbers:
        if number >= 0:
            filtered_list_of_numbers.append(number)
else:
    print("Invalid command.")
print(filtered_list_of_numbers)