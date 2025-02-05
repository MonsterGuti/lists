number_of_rooms = int(input())
is_crowded = False
total_free_chairs = 0

for number_of_room in range(number_of_rooms):
    user_input = input().split()
    capacity = user_input[0]
    people = user_input[1]
    if int(people) > len(capacity):
        is_crowded = True
        needed_chairs_in_room = int(people) - len(capacity)
        print(f"{needed_chairs_in_room} more chairs needed in room {number_of_room + 1}")
    else:
        total_free_chairs += len(capacity) - int(people)

if not is_crowded:
    print(f"Game On, {total_free_chairs} free chairs left")
