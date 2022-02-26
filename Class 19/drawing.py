import pygame

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)

cyan = pygame.Color((0, 255, 255))

pygame.draw.line(screen, (0, 255, 0), (0,0), (500, 500), 10)

pygame.draw.line(screen, cyan, (500, 0), (0, 500), 10)

pygame.draw.rect(screen, (255, 0, 0), (150, 240, 200, 20))
pygame.draw.rect(screen, (255, 0, 0), (240, 150, 20, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.time.Clock().tick(20)
    pygame.display.flip()
