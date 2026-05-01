#BASIC PYGAME WINDOW, GRID
import pygame
import sys

pygame.init()

WIDTH = 500
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

CELL_SIZE = 150
board_x = 25
board_y = 75

def draw_grid():
    # background
    screen.fill((245, 245, 245))

    # vertical lines
    for i in range(1, 3):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (board_x + i * CELL_SIZE, board_y),
            (board_x + i * CELL_SIZE, board_y + 450),
            5
        )

    # horizontal lines
    for i in range(1, 3):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (board_x, board_y + i * CELL_SIZE),
            (board_x + 450, board_y + i * CELL_SIZE),
            5
        )

while True:
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()