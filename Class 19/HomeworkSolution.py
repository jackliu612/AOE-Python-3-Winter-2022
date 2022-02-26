import pygame
import random


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    print(r, g, b)
    return pygame.Color((r, g, b))


pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)

frame_count = 0

while True:
    print(frame_count)
    pygame.time.Clock().tick(20)
    if frame_count % 100 == 0:
        screen.fill(get_random_color())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    frame_count += 1

    pygame.display.flip()
