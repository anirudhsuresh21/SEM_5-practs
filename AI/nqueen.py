

def solve_util(board,col):
    if col>=len(board):
        return True
    
    for i in range(len(board)):
        if is_safe(board,i,col):
            board[i][col] = 1
            if solve_util(board,col+1):
                return True
            board[i][col] = 0
    return False


def is_safe(board,row,col):
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
        
    for i,j in zip(range(row,len(board),1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
        
    return True


def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_util(board,0):
        print("Solution does not exist")
        return False
    for row in board:
        print(" ".join(str(x) for x in row))
    print()
    return True


if __name__ == "__main__":

    n = 4 # You can change the value of n for different board sizes
    solve_nqueens(n)



