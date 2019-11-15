from math import pi
from random import randint, random
from time import time

import pygame
from pygame import Color
from Sprites import Button

GREEN = (19, 255, 140)
GREY = (209, 210 ,210)
WHITE = (254, 255, 255)
RED = (254, 0, 0)
PURPLE = (254, 0, 255)
pygame.font.init()
myfont = pygame.font.SysFont('delicious', 90)
title = myfont.render('Alien Dress Up', False, PURPLE)

 #add other buttons


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
    screen.blit(title, (100, 0))
    clothing_items = ["hat_icon.png", "shirt-icon.png", "shoe-icon.png", "pant-icon.png", "dress-icon.png"]
    for item in clothing_items:
        x = 40
        y += 50
        screen.blit(Button.image, Button.rect)

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
