import pygame

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)

classicmusic = pygame.mixer.music
classicmusic.load("scarboroughFair.mp3")
classicmusic.set_volume(1)
classicmusic.play(loops=5, start=10)

ticks = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.Clock().tick(10)

    print(classicmusic.get_pos())

    if ticks == 40:
        classicmusic.fadeout(1000)
    ticks += 1
    pygame.display.flip()
