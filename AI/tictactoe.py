import random

def printBoard(board):
    """Prints the board in a readable format."""
    for row in board:
        print(" | ".join([cell if cell != "" else " " for cell in row]))
        print("-" * 9)  # Horizontal separator

def checkWin(board):
    """Checks all possible winning conditions."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

def inputAI(board):
    """Randomly selects an empty cell for AI's move."""
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == "":
            board[row][col] = "O"  # AI uses 'O'
            print(f"AI placed 'O' at ({row}, {col})")
            break

def inputHuman(board, row, col):
    """Places 'X' on the board if the spot is empty."""
    if board[row][col] == "":
        board[row][col] = "X"
        return True
    else:
        print("Cell already occupied! Try again.")
        return False

def solve(board):
    """Main game loop."""
    while True:
        # Get human input
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 2.")
            continue

        # Place human's move
        if inputHuman(board, row, col):
            printBoard(board)
            if checkWin(board):
                print("You Win!")
                break

            # AI's turn
            inputAI(board)
            printBoard(board)
            if checkWin(board):
                print("AI Wins!")
                break

        # Check for a draw (if all cells are filled)
        if all(cell != "" for row in board for cell in row):
            print("It's a draw!")
            break

# Initialize empty board
board = [["", "", ""], ["", "", ""], ["", "", ""]]

print("Welcome to Tic-Tac-Toe!")
printBoard(board)
solve(board)
