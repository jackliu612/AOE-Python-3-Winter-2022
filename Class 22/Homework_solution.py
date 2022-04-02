import pygame

pygame.init()
screen_width = 500
screen_height = 500
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

RED = pygame.Color([255, 0, 0])
BLACK = pygame.Color([0, 0, 0])

rect_x = 250
rect_y = 100

goRight = False
width = 50

goUp = False
height = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.time.Clock().tick(120)

    screen.fill(BLACK)
    # Draw the rectangle
    pygame.draw.rect(screen, RED, [rect_x, rect_y, width, height])
    if goRight:
        rect_x = rect_x + 1
    else:
        rect_x = rect_x - 1

    if goUp:
        # goUp is True here
        rect_y = rect_y - 1
    else:
        # goUp is False here
        rect_y = rect_y + 1

    if rect_x >= screen_width-width:
        goRight = False
    if rect_x <= 0:
        goRight = True

    if rect_y >= screen_height-height:
        # we at the bottom of the screen!
        goUp = True
    if rect_y <= 0:
        goUp = False

    pygame.display.flip()
