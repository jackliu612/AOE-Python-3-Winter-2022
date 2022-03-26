import pygame
import random

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)

classicmusic=pygame.mixer.music
classicmusic.load("scarboroughFair.mp3")
classicmusic.set_volume(1)
classicmusic.play(start=5, fade_ms=2000)

ticks = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.Clock().tick(20)
    if 5000 < pygame.time.get_ticks() < 10000:
        classicmusic.pause()
    elif pygame.time.get_ticks()>10000:
        classicmusic.unpause()


    pygame.display.flip()
