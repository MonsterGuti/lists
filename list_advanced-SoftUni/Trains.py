number_of_wagons = int(input())
waggons_list = []
for _ in range(number_of_wagons):
    waggons_list.append(0)
while True:
    command = input()
    if command == "End":
        break
    else:
        command_items = command.split()
        if len(command.split()) == 2:
            action = command_items[0]
            quantity = int(command_items[1])
            if action == "add":
                waggons_list[len(waggons_list) - 1] += quantity
        elif len(command.split()) == 3:
            action = command_items[0]
            wagon = int(command_items[1])
            quantity = int(command_items[2])
            if action == "insert":
                waggons_list[wagon] += quantity
            elif action == "leave":
                waggons_list[wagon] -= quantity
print(waggons_list)
