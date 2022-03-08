#https://www10.lunapic.com/editor/ to edit backgrounds
import pygame
import random


pygame.init()

black = (0,0,0)
white = (255,255,255)

background = pygame.image.load("Visual Studio Code/Python/Pokemon_battle/Images/background.jpg")
background = pygame.transform.scale(background, (873*0.5,479*0.5))
squirtle = pygame.image.load("Visual Studio Code/Python/Pokemon_battle/Images/squirtle.png")
squirtle = pygame.transform.scale(squirtle, (50, 80))
squirtle = pygame.transform.flip(squirtle, 180, 0) 
charmender = pygame.image.load("Visual Studio Code/Python/Pokemon_battle/Images/charmender.png")
charmender = pygame.transform.scale(charmender, (50, 80))
myfont = pygame.font.SysFont("Comic Sans MS", 20)
title = myfont.render("WELCOME TO POKEMON ROYALE", 1, black)



SCREEN = pygame.display.set_mode((873*0.5,479*0.5))
FPS = 50

def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def draw_objects():
    SCREEN.blit(background,(0,0))
    SCREEN.blit(squirtle,(squirtle_x, squirtle_y))
    SCREEN.blit(charmender, (charmender_x, charmender_y))
    SCREEN.blit(title, (title_x,title_y))


def start():
    global squirtle_x, squirtle_y, squirtle_vel, charmender_x, charmender_y, title_x, title_y
    squirtle_x, squirtle_y = 200*0.5,240*0.5
    charmender_x, charmender_y = 600*0.5, 240*0.5
    squirtle_vel = 0
    title_x, title_y = 50, 20

start()

running = True

while running:
    draw_objects()
    update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False