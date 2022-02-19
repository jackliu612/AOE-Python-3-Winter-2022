import pygame
import time
import random

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AOE Cool Game")


crashed = False
count = 0
starttime = time.time()
print(pygame.time.get_ticks() )

r_val = random.randint(0, 255)
g_val = random.randint(0, 255)
b_val = random.randint(0, 255)

# 241, 189, 255
rgb_vals = (r_val, g_val, b_val)
c = pygame.Color(rgb_vals)
print(c.r)
print(c.g)
print(c.b)
screen.fill(c)

while not crashed:
    pygame.time.Clock().tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    pygame.display.flip()

endtime = time.time()
print(pygame.time.get_ticks() )