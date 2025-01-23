n = int(input())
positive_list = []
negative_list = []
odd_list = []
even_list = []
for i in range(n):
    num = int(input())
    if num >= 0:
        positive_list.append(num)
    else:
        negative_list.append(num)
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
command = input()
if command == "positive":
    print(positive_list)
elif command == "negative":
    print(negative_list)
elif command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
else:
    print("Invalid command.")