first_string = input().split(", ")
second_string = input().split(", ")
mutual_list = []

for i in first_string:
    for j in second_string:
        if i in j:
            mutual_list.append(i)
            break

print(mutual_list)
