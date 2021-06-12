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
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print("| ",end="")
            if j == 8 and j != 0:
                print(board[i][j], end="\n")
            else:
                print(board[i][j], end=" ")

# Print initial Sudoku grid
print_board(grid)








# for i in range (len(board)):
#     if i % 3 and i != 0:
#         print("------------------------")

#     for j in range(len(board[0])):
#         if j % 3 == 0 and j != 0:
#             print(" | ", end="")
            
#             if j == 8:
#                 print(board[i][j])
#             else
#                 print(str(board[i][j]) + " ")

# Generate 9x9 grid
N = 9 

#for i in range N:


