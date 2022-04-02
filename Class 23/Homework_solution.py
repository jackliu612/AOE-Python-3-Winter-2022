# Music credits to https://patrickdearteaga.com
import pygame

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)

music_player = pygame.mixer.music
music_player.load("puzzle.ogg")
music_player.play()

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

    if ticks == 100:
        music_player.load("space.ogg")
        music_player.play(start=5)
    if ticks == 200:
        music_player.load("puzzle.ogg")
        music_player.play(start=10)

    pygame.display.flip()
