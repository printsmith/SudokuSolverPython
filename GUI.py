# GUI for SudokuSolver 

import pygame

# Initialize pygame and global variables for game 
WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Draws screen
def draw_window():

        WIN.fill(WHITE)
        drawGrid()
        pygame.display.update()

# Draws Sudoku grid
def drawGrid():
    size = int(WIDTH/9)
    for i in range(0, WIDTH, size):
        if i % 3 == 0 and i != 0:
            pygame.draw.lines(WIN, BLACK, False, [(i,0),(i,HEIGHT)], width = 6) 
        for j in range(0, HEIGHT, size):                
            rect = pygame.Rect(i, j, size, size)
            if j % 3 == 0 and j != 0:
                pygame.draw.lines(WIN, BLACK, False, [(0,j),(WIDTH,j)], width = 6) 
            pygame.draw.rect(WIN, BLACK, rect, 1)

# Main function
def main():
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    while run:
        drawGrid()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

# Selects square in grid
def select():


main()
pygame.quit()