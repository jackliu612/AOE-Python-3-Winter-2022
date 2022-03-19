import pygame

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)

cyan = pygame.Color([0, 255, 255])
window = pygame.Rect([0, 0, 250, 250])
pygame.draw.circle(screen, cyan, [250, 250], 100)

pygame.display.update(window)
# pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.Clock().tick(20)
