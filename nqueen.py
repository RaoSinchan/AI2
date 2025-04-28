print("Enter the number of queens")
N = int(input())

# Create an NxN chessboard initialized to 0
board = [[0]*N for _ in range(N)]

# Function to check if placing a queen at (i, j) will cause an attack
def attack(i, j):
    # Check row and column
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    
    # Check diagonals
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

# Function to solve the N-Queens problem using backtracking
def N_queens(n):
    # If all queens are placed, return True
    if n == N:
        return True
    
    # Try to place a queen on the board
    for i in range(0, N):
        for j in range(0, N):
            if not attack(i, j) and board[i][j] != 1:
                board[i][j] = 1
                if N_queens(n + 1):  # Place the next queen
                    return True
                board[i][j] = 0  # Backtrack if placing queen didn't work
    return False

# Start the N-Queens solution
if N_queens(0):
    for row in board:
        print(row)
else:
    print("No solution exists")
