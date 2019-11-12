from math import pi
from random import randint, random
from time import time

import pygame
from pygame import Color

from Sprites import Pants #add other buttons


background_color = Color(0, 175, 175)

screen = pygame.display.set_mode([1000, 1000])
screen.fill(background_color)

shape_start_size = 1

start_t = time()

size_incr_per_s = 150

fps = 30

gravity = 4



running = True
while running:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == pygame.MOUSEBUTTONUP:
            pass

    pygame.display.flip()
    pygame.time.delay(int(1000/fps))

pygame.quit()
