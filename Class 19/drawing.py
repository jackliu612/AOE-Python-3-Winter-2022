import pygame
import random

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)

screen.fill((0,0,255))
pygame.display.flip()

cyan = pygame.Color((0, 255, 255))

pygame.draw.line(screen, (0, 255, 0), (0,0), (500, 500), 10)

pygame.draw.line(screen, cyan, (500, 0), (0, 500), 10)

pygame.draw.rect(screen, (255, 0, 0), (150, 240, 200, 20), 5)
pygame.draw.rect(screen, (255, 0, 0), (240, 150, 20, 200), 5000000)

my_rect = pygame.Rect([355, 350, 100, 70])

# myrect=pygame.draw.rect(screen, (255, 0, 0), [155, 200, 100, 70], 5)
# mysurface=screen.subsurface(myrect)
# pygame.draw.line(mysurface, (0, 255, 0), (0,0), (500, 500), 10)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    pygame.time.Clock().tick(1)
    # pygame.display.flip()
    pygame.display.update(my_rect)
