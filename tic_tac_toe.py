import math

# Initialize the board
board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n-------------")

def is_moves_left():
    return any(cell == ' ' for row in board for cell in row)

def evaluate():
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return 10 if row[0] == 'O' else -10
    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return 10 if board[0][col] == 'O' else -10
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return 10 if board[0][0] == 'O' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return 10 if board[0][2] == 'O' else -10
    return 0

def minimax(depth, is_max, alpha, beta):
    score = evaluate()
    if score != 0:
        return score
    if not is_moves_left():
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(depth + 1, False, alpha, beta))
                    board[i][j] = ' '
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(depth + 1, True, alpha, beta))
                    board[i][j] = ' '
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move():
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def check_winner():
    score = evaluate()
    if score == 10:
        return "AI wins!"
    elif score == -10:
        return "You win!"
    elif not is_moves_left():
        return "It's a draw!"
    return None

# Game Loop
def play_game():
    print("You are 'X'. AI is 'O'.")
    print_board()

    while True:
        # Human move
        try:
            row, col = map(int, input("Enter your move (row and col 0-2): ").split())
        except:
            print("Please enter two numbers separated by a space.")
            continue

        if row not in range(3) or col not in range(3) or board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue

        board[row][col] = 'X'
        print_board()

        result = check_winner()
        if result:
            print(result)
            break

        # AI move
        print("AI is making a move...")
        ai_move = find_best_move()
        board[ai_move[0]][ai_move[1]] = 'O'
        print_board()

        result = check_winner()
        if result:
            print(result)
            break

# Run the game
play_game()