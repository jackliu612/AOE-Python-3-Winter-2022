import pygame

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)

classicmusic = pygame.mixer.music
classicmusic.load("../Class 22/scarboroughFair.mp3")
classicmusic.play()

ticks = 0

def displaytext(texttodisplay):
    myfont = pygame.font.SysFont("comicsansms", 18)
    mytext = myfont.render(texttodisplay, True, (255, 0, 0))
    screen.blit(mytext, (10, 50))

musiclyrics=["Are you going to Scarborough Fair?",
    "Parsley, sage, rosemary and thyme",
    "Remember me to one who lives there",
    "For she once was a true love of mine"]

startpos=[10000,17200,25800,33000]
displaytext("We will display the lyrics here")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.Clock().tick(10)

    print(classicmusic.get_pos())

    try:
        if (classicmusic.get_pos()>=startpos[0]):
            displaytext(musiclyrics[0])
            del startpos[0]
            del musiclyrics[0]
    except:
        pass

    ticks += 1
    pygame.display.flip()
