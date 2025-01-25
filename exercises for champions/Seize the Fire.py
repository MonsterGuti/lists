fire_information = input().split("#")
total_water = int(input())
total_effort = total_fire = 0
print("Cells:")
for command in fire_information:
    command_parts = command.split(" = ")
    command_level = command_parts[0]
    command_value = int(command_parts[1])
    if command_level == "High":
        if 81 <= command_value <= 125 and total_water >= command_value:
            total_water -= command_value
            total_fire += command_value
            total_effort += 0.25 * command_value
            print(f" - {command_value}")
    elif command_level == "Medium":
        if 51 <= command_value <= 80 and total_water >= command_value:
            total_water -= command_value
            total_fire += command_value
            total_effort += 0.25 * command_value
            print(f" - {command_value}")
    elif command_level == "Low":
        if 1 <= command_value <= 50 and total_water >= command_value:
            total_water -= command_value
            total_fire += command_value
            total_effort += 0.25 * command_value
            print(f" - {command_value}")
print(f"Effort: {(total_effort):.2f}")
print(f"Total Fire: {total_fire}")
