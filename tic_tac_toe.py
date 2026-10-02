def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    # Check main diagonal
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    # Check anti-diagonal
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


# Initialize 3x3 empty board
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

# Up to 9 moves in a game
for turn in range(9):
    print(f"\nPlayer {current_player}'s turn:")
    print_board(board)

    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == " ":
                    board[row][col] = current_player
                    break
                else:
                    print("Cell already occupied. Try again.")
            else:
                print("Invalid input! Please enter numbers between 0 and 2.")
        except ValueError:
            print("Please enter valid integers.")

    if check_winner(board):
        print_board(board)
        print(f"\nPlayer {current_player} wins!")
        break

    # Switch turns
    current_player = "O" if current_player == "X" else "X"
else:
    # Executes only if the loop finishes 9 turns without a break
    print_board(board)
    print("\nGame Draw!")