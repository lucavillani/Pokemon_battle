import pygame
import random

pygame.init()

black = (0,0,0)
white = (255,255,255)

background = pygame.image.load("Visual Studio Code/Python/Pokemon_battle/Images/background.jpg")
squirtle = pygame.image.load("Visual Studio Code/Python/Pokemon_battle/Images/squirtle.png")

SCREEN = pygame.display.set_mode((873, 479))
FPS = 50

def update():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def draw_objects():
    SCREEN.blit(background,(0,0))
    SCREEN.blit(squirtle,(squirtle_x, squirtle_y))


def start():
    global squirtle_x, squirtle_y, squirtle_vel
    squirtle_x, squirtle_y = 0,0
    squirtle_vel = 0

start()

running = True

while running:
    draw_objects()
    update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False