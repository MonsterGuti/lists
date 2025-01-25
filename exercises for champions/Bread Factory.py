total_energy = 100
total_coins = 100
events = input().split("|")
bakery_open = True
for current_event in events:
    event_items = current_event.split("-")
    event_type, event_value = event_items[0], int(event_items[1])
    if event_type == "rest":
        initial_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif event_type == "order":
        if total_energy >= 30:
            total_coins += event_value
            total_energy -= 30
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            bakery_open = False
            break
if bakery_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")