import pygame

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
print(pygame.mixer.get_num_channels())

cat = pygame.mixer.Sound("cat.ogg")
bird = pygame.mixer.Sound("bird.ogg")

catchannel = pygame.mixer.Channel(0)
catchannel.set_volume(.8)
birdchannel = pygame.mixer.Channel(1)
birdchannel.set_volume(.3)

birdchannel.play(bird, -1)

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

    # print("cat channels:", cat.get_num_channels())
    # print("is cat channel busy?:", catchannel.get_busy())

    if ticks == 60:
        birdchannel.pause()
        # bird.play()

    if ticks == 120:
        birdchannel.unpause()
        catchannel.play(cat)

    if ticks == 200:
        pygame.mixer.pause()

    pygame.display.flip()
