import pygame
import random

pygame.init()
screen_width = 500
size = (screen_width, 500)
screen = pygame.display.set_mode(size)

RED = pygame.Color([255, 0, 0])
BLACK = pygame.Color([0, 0, 0])
# [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
rect_x = 250

goRight = False
width = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.time.Clock().tick(120)

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [rect_x, 250, width, 50])
    if goRight:
        rect_x = rect_x + 1
    else:
        rect_x = rect_x - 1

    if rect_x >= screen_width-width:
        goRight = False
    if rect_x <= 0:
        goRight = True

    pygame.display.flip()
