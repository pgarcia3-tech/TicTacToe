#BASIC PYGAME WINDOW, GRID
import pygame
import sys
import random

import TTTbackend

#initialize pygame
pygame.init()

#window dimensions
WIDTH = 500
HEIGHT = 650

#display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# cell size in grid
CELL_SIZE = 150
board_x = 25
board_y = 105

#fonts
title_font = pygame.font.SysFont(None, 52)
font = pygame.font.SysFont(None, 100)
med_font = pygame.font.SysFont(None, 28)
small_font = pygame.font.SysFont(None, 26)

#import ladybug and beetle drawings
ladybug_img = pygame.image.load("ladybug.png")
beetle_img = pygame.image.load("beetle.png")
mantis_img = pygame.image.load("mantis2.png")
cloud_img = pygame.image.load("cloud.png")

#resize
ladybug_img = pygame.transform.scale(ladybug_img, (100, 100))
beetle_img = pygame.transform.scale(beetle_img, (100 ,100 ))
mantis_img = pygame.transform.scale(mantis_img, (80, 80))
cloud_img = pygame.transform.scale(cloud_img, (70, 70))

#ladybug celebration
celebration_ladybugs = []
for i in range(40):
    celebration_ladybugs.append([
        random.randint(0, WIDTH - 50),
        random.randint(-300, 0),
        random.randint(6, 12)
    ])

#thunderstorm
storm_active = False
storm_end_time = 0

#scarab swarm 
scarab_swarm_x = -400


def draw_grid():
    # background 
    screen.fill((117, 170, 255))

    # vertical lines
    for i in range(1, 3):
        pygame.draw.line(
            screen,
            (30,90,30), # black color
            (board_x + i * CELL_SIZE, board_y), # start 
            (board_x + i * CELL_SIZE, board_y + 450), # end 
            5 # thickness
        )

    # horizontal lines
    for i in range(1, 3):
        pygame.draw.line(
            screen,
            (30,90,30),
            (board_x, board_y + i * CELL_SIZE),
            (board_x + 450, board_y + i * CELL_SIZE),
            5
        )

def draw_marks(board):
        #draw X and O on the grid 

        for row in range(3):
            for col in range(3):
                mark = board[row][col]
                if mark != "": #if mark isnt empty

                    # text = font.render(mark, True, color)
                    x = board_x + col * CELL_SIZE + CELL_SIZE // 2 - 50
                    y = board_y + row * CELL_SIZE + CELL_SIZE // 2 - 50

                    if mark == "X":
                        screen.blit(ladybug_img, (x, y))
                    else:
                        screen.blit(beetle_img, (x, y))

def draw_restart_button():
    button_color = (200, 240, 200)
    pygame.draw.rect(screen, button_color, (160, 600, 180, 35), border_radius=30)
    pygame.draw.rect(screen, (0,0,0), (160, 600, 180, 35), 2, border_radius=30)

    text = small_font.render("THUNDERSTORM", True, (0,0,0))
    screen.blit(
        text,
        (
            160 + 180 // 2- text.get_width() // 2,
            600 + 35 // 2- text.get_height() // 2
        )
    )

def draw_title():
    title = title_font.render("Tic Tac Toe", True, (30, 30, 30))

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 10))
    #mantis image - he wants YOU to protect his garden
    screen.blit(mantis_img, (15, 8))
 
#status at the bottom!
def draw_status():
    if TTTbackend.winner == "X":
        message = "Ladybugs win :D "
    elif TTTbackend.winner == "O":
        message = "Scarabs feast tonight >:D "
    elif TTTbackend.winner == "Tie":
        message = "The garden rests..."
    else:
        message = "Defend Old Mr. Mantis' Garden"
    status_text = med_font.render(message, True, (40, 70, 40))
    screen.blit(status_text, (WIDTH // 2 - status_text.get_width() // 2, 55))

    score_text = small_font.render(
        f"Ladybugs: {TTTbackend.player_score}   Scarabs: {TTTbackend.computer_score}   Ties {TTTbackend.ties}", True, (0, 0, 0) )
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 575))
#cloud for decoration
def draw_cloud():
    screen.blit(cloud_img, (390, 5))
    
# ladybugs rain every time they win
def draw_ladybug_celebration():
    if TTTbackend.winner == "X":
        for bug in celebration_ladybugs:
            x, y, speed = bug

            screen.blit(
                pygame.transform.scale(ladybug_img, (45, 45)),
                (x, y)
            )

            bug[1] += speed

            if bug[1] > HEIGHT:
                bug[0] = random.randint(0, WIDTH - 45)
                bug[1] = random.randint(-200, -45)
                bug[2] = random.randint(6, 12)

# flashing red every time the scarabs win
def draw_scarab_swarm():
    global scarab_swarm_x
    if TTTbackend.winner == "O":
        for i in range(30):
            x = scarab_swarm_x + random.randint(0, 900)
            y = random.randint(90, 500)

            screen.blit(
                pygame.transform.scale(beetle_img, (60, 60)),
                (x, y)
            )

        scarab_swarm_x += 10
        if scarab_swarm_x > WIDTH:
            scarab_swarm_x = -500
    else:
        scarab_swarm_x = -500

#thunderstorm hard reset
def draw_thunderstorm():
    if storm_active:
        current_time = pygame.time.get_ticks()
        # flashing effect
        if (current_time // 80) % 2 == 0:
            screen.fill((255, 255, 120)) #yellow flash
        else:
            screen.fill((240, 240, 240))  # white flash


            
# game loop, runs continuously
while True:
    TTTbackend.update_computer()
    TTTbackend.update_reset()
    draw_grid()
    
    draw_marks(TTTbackend.board)
    draw_title()
    draw_status()
    draw_restart_button()
    draw_cloud()
    draw_ladybug_celebration()
    draw_scarab_swarm()
    draw_thunderstorm()
    
# check for event, closing window, etc
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 160 <= x <= 340 and 600 <= y <= 635:
                storm_active = True
                storm_end_time = pygame.time.get_ticks() + 800
                TTTbackend.reset_all()
            else:
                TTTbackend.handle_click(event.pos)
    current_time = pygame.time.get_ticks()
    if storm_active and current_time >= storm_end_time:
        storm_active = False


# update display
    pygame.display.update()