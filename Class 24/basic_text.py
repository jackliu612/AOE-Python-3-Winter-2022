import pygame

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)

ticks = 0
seconds = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.time.Clock().tick(20)
    ticks += 1
    if ticks % 20 == 0:
        seconds += 1
        print("Now at second:", seconds)

    pygame.display.flip()
