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

alien = pygame.Rect(750,250,100,500)
shirt = pygame.Rect(750,400,200,100)


running = True
while running:
    screen.fill(background_color)
    pygame.draw.rect(screen, Color(0,0,0),alien)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,Color(255,255,255),shirt)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            pass


    pygame.time.delay(int(1000/fps))

pygame.quit()
