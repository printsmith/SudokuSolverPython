#
#   Sudoku Solver
#   Tyler Kalinowicz
#

# Populate initial Sudoku board
grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
]


# Function prints Sudoku board with grid lines
def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("----------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ",end="")
            if j == 8 and j != 0:
                print(board[i][j], end="\n")
            else:
                print(board[i][j], end=" ")

# Print initial Sudoku grid
print_board(grid)

# Finds empty squares in board
def find_empty(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return(i, j) # returns the row and column of empty squares

def SudokuSolver(board):

    # Check if board is alrady solved, otherwise find first empty position to begin solving
    if not find_empty(board):
        return True
    else:
        find = find_empty(board)

    # Run through numbers 1-9 and check validity 
    for i in range(1,10):
        # Pass in board, num and empty space coordinates (find) to isValid
        if isValid(board, i, find):
            board[find[0]][find[1]] = i
    
    print_board(board)


# Checks if current number is already in row. 
# num is a numbr 1-9 being tested, pos is the current position in the sudoku grid found via isValid
def isValid(board, num, pos):


    # pos[0] = row of test point
    row = pos[0]
    # pos[1] = column of test point
    col = pos[1]

    # Check row
    for i in range(len(board[0])):
        print(board[row][i])
        if board[row][i] == num:
            return False
    
    # Check column
    # for i in range(len(board[0])):
    #     if board[i][col] == num:
    #         return False

    return True

SudokuSolver(grid)
