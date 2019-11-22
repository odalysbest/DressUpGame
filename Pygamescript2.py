from enum import Enum
from math import pi
from random import randint, random
from time import time

import pygame
from pygame import Color
from Sprites import Button
from PyMain import PyManMain
from PyMain import newScreen


GREEN = (19, 255, 140)
GREY = (209, 210, 210)
WHITE = (254, 255, 255)
RED = (254, 0, 0)
PURPLE = (254, 0, 255)
pygame.font.init()
myfont = pygame.font.SysFont('delicious', 90)
title = myfont.render('Alien Dress Up', False, PURPLE)

# add other buttons


background_color = Color(0, 175, 175)

screen = pygame.display.set_mode([1000, 1000])
screen.fill(background_color)

running = True


class States(Enum):
    MENU = 0
    HAT = 1
    SHIRTS = 2
    SHOES = 3
    PANTS = 4
    DRESS = 5


list_hats = ['earmuff.png', 'necklace.png']
x = 250
y = 99
hats = []
for item in list_hats:
    hats.append(Button(item, x, y, item.split('.')[-1]))
    x += 150

list_shirts = ['crop-top.png', 'orange-shirt.png', 'pink-sweater.png']
x = 250
y = 200
shirts = []
for item in list_shirts:
    shirts.append(Button(item, x, y, item.split('.')[-1]))
    x += 150


list_shoes = ['boots.png', 'grey-shoes.png']
x = 250
y = 300
shoes = []
for item in list_shoes:
    shoes.append(Button(item, x, y, item.split('.')[-1]))
    x += 150

list_pants = ['jeans.png', 'red-skirt.png']
x = 250
y = 400
pants = []
for item in list_pants:
    pants.append(Button(item, x, y, item.split('.')[-1]))
    x += 150


list_dresses = ['overalls.png', 'purple-dress.png']
x = 250
y = 500
dresses = []
for item in list_dresses:
    dresses.append(Button(item, x, y, item.split('.')[-1]))
    x += 150

hatButton = Button("hat-icon.png", 100, 100, "hat-icon")
shirtButton = Button("shirt-icon.png", 100, 200, "shirt-icon")
shoeButton = Button("shoe-icon.png", 100, 300, "shoe-icon")
pantButton = Button("pant-icon.png", 100, 400, "pant-icon")
dressButton = Button("dress-icon.png", 100, 500, "dress-icon")

state = States.MENU


class StateMachine:
    currentState = States.MENU

    def changeState(self, state):
        self.currentState = state


stateMachine = StateMachine()

hatButton.function = lambda: stateMachine.changeState(States.HAT)
shirtButton.function = lambda: stateMachine.changeState(States.SHIRTS)
shoeButton.function = lambda: stateMachine.changeState(States.SHOES)
pantButton.function = lambda: stateMachine.changeState(States.PANTS)
dressButton.function = lambda: stateMachine.changeState(States.DRESS)

while running:
    screen.fill(background_color)
    screen.blit(title, (250, 0))
    screen.blit(pygame.transform.scale(pygame.image.load('drawings/alien-base.png'), (400, 400)), [600, 200])
    screen.blit(hatButton.image, hatButton.pos)
    screen.blit(shirtButton.image, shirtButton.pos)
    screen.blit(shoeButton.image, shoeButton.pos)
    screen.blit(pantButton.image, pantButton.pos)
    screen.blit(dressButton.image, dressButton.pos)
    for event in pygame.event.get():
        hatButton.get_event(event)
        shirtButton.get_event(event)
        shoeButton.get_event(event)
        pantButton.get_event(event)
        dressButton.get_event(event)
        if event.type == pygame.QUIT:
            running = False
            pass

    if stateMachine.currentState == States.MENU:
        pass
    elif stateMachine.currentState == States.HAT:
        for button in hats:
            screen.blit(button.image, button.pos)
    elif stateMachine.currentState == States.SHIRTS:
        for button in shirts:
            screen.blit(button.image, button.pos)
    elif stateMachine.currentState == States.SHOES:
        for button in shoes:
            screen.blit(button.image, button.pos)
    elif stateMachine.currentState == States.PANTS:
        for button in pants:
            screen.blit(button.image, button.pos)
    elif stateMachine.currentState == States.DRESS:
        for button in dresses:
            screen.blit(button.image, button.pos)

    pygame.display.flip()
    pygame.time.delay(int(1000 / 60))

pygame.quit()

