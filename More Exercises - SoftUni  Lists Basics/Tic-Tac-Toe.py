first_line = input().split()
second_line = input().split()
third_line = input().split()

board = [first_line, second_line, third_line]

for row in board:
    if row[0] == row[1] == row[2] == "1":
        print("First player won")
        exit()
    elif row[0] == row[1] == row[2] == "2":
        print("Second player won")
        exit()

for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] == "1":
        print("First player won")
        exit()
    elif board[0][col] == board[1][col] == board[2][col] == "2":
        print("Second player won")
        exit()

if board[0][0] == board[1][1] == board[2][2] == "1" or board[0][2] == board[1][1] == board[2][0] == "1":
    print("First player won")
elif board[0][0] == board[1][1] == board[2][2] == "2" or board[0][2] == board[1][1] == board[2][0] == "2":
    print("Second player won")
else:
    print("Draw!")
