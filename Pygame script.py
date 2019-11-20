from math import pi
from random import randint, random
from time import time

import pygame
from pygame import Color
from Sprites import Button
from PyMain import PyManMain
from PyMain import newScreen

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

running = True

clothing_items = ["hat-icon.png", "shirt-icon.png", "shoe-icon.png", "pant-icon.png", "dress-icon.png"]
x = 100
y = 100
buttons = []
for item in clothing_items:
    buttons.append(Button(item, x, y, item.split('.')[0]))
    y += 100

while running:
    screen.fill(background_color)
    screen.blit(title, (100, 0))
    for button in buttons:
        screen.blit(button.image, button.pos)
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
#FOLLOWING CODE IS FOR SCREEN BUTTONS TO CHANGE: background, reset clothes,
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()
   if menu == 'menu':
       # Displays main options menu
       # Looks for key presses to navigate through options (works great)
       # Looks for mouse position and presses:
       if 90 < mouse[0] < 110 and 90 < mouse[1] < 110:
           if click[0] == 1:
               menu = 'bdg'

   if menu == 'bgd':
       bgd_items = []
