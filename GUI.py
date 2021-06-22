# GUI for SudokuGame

import pygame
pygame.font.init()

# Initialize pygame and global variables for game 
width, height = 900, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
FPS = 60

class Grid:
    # Class to store grid and solve/check
    board = [
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

    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.cells = [[Cell(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.win = win
        self.model = None
        self.selected = None
        self.update_model()

    def update_model(self):
        self.model = [[(self.cells[i][j], i, j, width, height) for j in range(self.cols)] for i in range(self.rows)]

    def draw(self):
        size = self.width / 9

        # Draw the grid lines
        for i in range(self.rows):
            if i % 3 == 0 and i != 0:
                t = 6
            else:
                t = 1
            pygame.draw.line(self.win, BLACK, (0, i*size), (self.width, i*size), t)
            pygame.draw.line(self.win, BLACK, (i*size, 0), (i*size, self.height), t)
        
        # Draw the cells
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.win)
    

class Cell:
    # Class to store data of single cell in Sudoku board

    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        # Draw cell and values within
        font = pygame.font.SysFont("calibri", 60)
        size = self.width / 9
        x = self.col * size
        y = self.row * size

        # Write in temp or value
        if self.temp != 0 and self.value == 0:
            num = font.render(str(self.temp), True, GREY)
            win.blit(num, (x, y))
        elif self.value != 0:
            num = font.render(str(self.value), True, BLACK)
            win.blit(num, (x + (size/2), y + (size/2)))

    def set(self, val):
        # Sets value of selected cell
        self.value = val

    def set_temp(self, val):
        # Sets temporary value of selected cell
        self.temp = val

def draw_window(win, board):
    # Draw game window
    win.fill(WHITE)
    #font = pygame.font.SysFont("calibri", 60) 
    board.draw()

# Main function
def main():
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")
    board = Grid(9, 9, width, height, win)
    clock = pygame.time.Clock()
    run = True
    key = None
   
    while run:
        # main game loop
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                # Check which key is pressed and what action is associated with it
                if event.key == pygame.K_1 or pygame.K_KP1:
                    key = 1
                if event.key == pygame.K_2 or pygame.K_KP2:
                    key = 2
                if event.key == pygame.K_3 or pygame.K_KP3:
                    key = 3
                if event.key == pygame.K_4 or pygame.K_KP4:
                    key = 4
                if event.key == pygame.K_5 or pygame.K_KP5:
                    key = 5
                if event.key == pygame.K_6 or pygame.K_KP6:
                    key = 6
                if event.key == pygame.K_7 or pygame.K_KP7:
                    key = 7
                if event.key == pygame.K_8 or pygame.K_KP8:
                    key = 8
                if event.key == pygame.K_9 or pygame.K_KP9:
                    key = 9
                if event.key == pygame.K_BACKSPACE or pygame.K_DELETE:
                    board.clear()
                    key = None

        draw_window(win, board)
        pygame.display.update()


main()
pygame.quit()