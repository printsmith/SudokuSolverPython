# Main Sudoku game code

import math
import GUI

# Finds empty squares in board
def find_empty(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return(i, j) # returns the row and column of empty squares

# Checks validity
def isValid(board, num, pos):

    # pos[0] = row of test point
    row = pos[0]
    # pos[1] = column of test point
    col = pos[1]

    # Check row
    for i in range(len(board[0])):
        if board[row][i] == num:
            return False
    
    # Check column
    for i in range(len(board[0])):
        if board[i][col] == num:
            return False

    # Check square by breaking sudoku into a 3x3 grid using the row and col, grid size is sqrt of board length
    n = int(math.sqrt(len(board[0])))
    gridPos = [row//n, col//n]

    for i in range(len(board[0])):
        for j in range(len(board[0])):
            testPos = [i//n, j//n]
            if testPos == gridPos:
                if board[i][j] == num:
                    return False
    
    return True

# Solves board state
def solve(board):

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
            if solve(board): 
                return True
            board[find[0]][find[1]] = 0 # backtracking to return current state to 0 if it is invalid
    return False

def main():
    GUI.main()
