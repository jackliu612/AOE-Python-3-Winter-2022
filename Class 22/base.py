import pygame
import random

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)

classicmusic=pygame.mixer.music
classicmusic.load("scarboroughFair.mp3")
classicmusic.play()

ticks = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.Clock().tick(20)


    pygame.display.flip()
