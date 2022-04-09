# Music credits to https://patrickdearteaga.com
import pygame

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)

music_player = pygame.mixer.music
music_player.load("../Class 23/puzzle.ogg")
music_player.set_volume(.3)


cat = pygame.mixer.Sound("../Class 23/cat.ogg")
bird = pygame.mixer.Sound("../Class 23/bird.ogg")

catchannel = pygame.mixer.Channel(3)
birdchannel = pygame.mixer.Channel(4)

last_played = "cat"

music_player.play()
catchannel.play(cat)



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

    if not catchannel.get_busy() and not birdchannel.get_busy():
        if last_played == 'cat':
            print("Switching to bird")
            birdchannel.play(bird)
            last_played = 'bird'
        elif last_played == 'bird':
            print("Switching to cat")
            catchannel.play(cat)
            last_played = 'cat'

    pygame.display.flip()
