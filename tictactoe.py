# Tic Tac Toe Console Version
# X starts first
def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print()

def check_win(board, player):
    # rows, cols, diagonals
    for i in range(3):
        if all(board[i][j]==player for j in range(3)):
            return True
        if all(board[j][i]==player for j in range(3)):
            return True
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        return True
    if board[0][2]==player and board[1][1]==player and board[2][0]==player:
        return True
    return False

def check_draw(board):
    return all(board[i][j]!=" " for i in range(3) for j in range(3))

def main():
    board = [[" "]*3 for _ in range(3)]
    turn = "X"
    print_board(board)

    while True:
        try:
            move = input(f"{turn}'s turn (row col 1-3): ")
            r,c = map(int, move.split())
            r -= 1; c -= 1
            if board[r][c] != " ":
                print("Cell occupied! Try again.")
                continue
            board[r][c] = turn
            print_board(board)

            if check_win(board, turn):
                print(f"{turn} wins!")
                break
            if check_draw(board):
                print("Draw!")
                break

            turn = "O" if turn=="X" else "X"

        except (ValueError, IndexError):
            print("Invalid input. Enter row and column numbers 1-3 separated by space.")

if __name__ == "__main__":
    main()
