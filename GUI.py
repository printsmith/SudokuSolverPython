# GUI for SudokuGame

import pygame

# Initialize pygame and global variables for game 
width, height = 900, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Populate initial Sudoku board
class Grid:
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
        self.boxes = [[Box(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.win = win
        self.model = None
        self.update_model()
        self.selected = None

    def update_model(self):
        self.model = []

    def drawGrid(self):
        size = self.width / 9
        for i in range(self.rows):
            if i % 3 == 0 and i != 0:
                t = 6
            else:
                t = 1
            pygame.draw.line(self.win, BLACK, (0, i*size), (self.width, i*size), t)
            pygame.draw.line(self.win, BLACK, (i*size, 0), (i*size, self.height), t)
            rect = pygame.Rect(i, i, size, size)
            pygame.draw.rect(self.win, BLACK, rect, 1)
    
    def clear(self):
        row, col = self.selected
        if self.box[row][col].value == 0:
            
class Box:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("calibri", 60)
        size = self.width / 9
        x = self.col * size
        y = self.row * size
    



# # Draws screen
# def draw_window():

#         WIN.fill(WHITE)
#         drawGrid()
#         pygame.display.update()

# Main function
def main():
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    run = True
    board = Grid(9, 9, width, height, win)
    key = None
   
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
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
                if event.key == pygame.K_BACKSPACE:
                    board.clear()
                    key = None



# Selects square in grid
#def select():


main()
pygame.quit()