import random
import os
import sys
import pygame
from pygame import Color
from Sprites import Button

GREY = (209, 210, 210)
RED = (254, 0, 0)

#https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
# create a text suface object,
# on which text is drawn on it.
text = font.render('FINISH', True, RED, GREY)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)


score = random.randint(0,100)
screen.blit(score, (100,100))
