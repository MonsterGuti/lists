names_of_gifts = input().split()
command_list = []

while True:
    command = input()
    if command == "No Money":
        break
    command_list.append(command)

for string in command_list:
    command_items = string.split()
    command_type = command_items[0]
    gift = command_items[1]

    if command_type == "OutOfStock":
        for i in range(len(names_of_gifts)):
            if names_of_gifts[i] == gift:
                names_of_gifts[i] = "None"

    elif command_type == "Required":
        index = int(command_items[2])
        if 0 <= index < len(names_of_gifts):
            names_of_gifts[index] = gift

    elif command_type == "JustInCase":
        names_of_gifts[-1] = gift

filtered_gifts = []
for gift in names_of_gifts:
    if gift != "None":
        print(gift, end=" ")

