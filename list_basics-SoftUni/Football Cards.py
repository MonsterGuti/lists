red_cards = input().split()
team_A = team_B = 0
checked_players = []

for player in red_cards:
    if player in checked_players:
        continue
    checked_players.append(player)

    if player.startswith("A"):
        team_A += 1
        if team_A > 4:
            print(f"Team A - {11 - team_A}; Team B - {11 - team_B}")
            print("Game was terminated")
            break
    elif player.startswith("B"):
        team_B += 1
        if team_B > 4:
            print(f"Team A - {11 - team_A}; Team B - {11 - team_B}")
            print("Game was terminated")
            break
else:
    print(f"Team A - {11 - team_A}; Team B - {11 - team_B}")
