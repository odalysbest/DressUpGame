from enum import Enum
from math import pi
from random import randint, random
from time import time

import pygame
from pygame import Color
from Sprites import Button

# from PyMain import PyManMain
# from PyMain import newScreen

GREEN = (19, 255, 140)
GREY = (209, 210, 210)
WHITE = (254, 255, 255)
RED = (254, 0, 0)
PURPLE = (254, 0, 255)
pygame.font.init()
myfont = pygame.font.SysFont('sansserif', 90)
title = myfont.render('Alien Dress Up', False, PURPLE)

# add other buttons
pygame.display.init()

screen = pygame.display.set_mode([1000, 1000])
background_color = Color(0, 175, 175)
bgdimage = pygame.transform.scale(pygame.image.load("start screen.png"), (1000, 1000))




running = True


class States(Enum):
    MENU = 0
    HAT = 1
    SHIRTS = 2
    SHOES = 3
    PANTS = 4
    DRESS = 5

class SubClothing(Enum):
    INITIAL = 0
    HAT1 = 1
    HAT2 = 2
    SHIRTS1 = 3
    SHIRTS2 = 4
    SHIRTS3 = 5
    SHOE1 = 6
    SHOE2 = 7
    PANTS1 = 8
    PANTS2 = 9
    DRESS1 = 10
    DRESS2 = 11


hatButton = Button("hat-icon.png", 100, 150, "hat-icon")
shirtButton = Button("shirt-icon.png", 100, 250, "shirt-icon")
shoeButton = Button("shoe-icon.png", 100, 350, "shoe-icon")
pantButton = Button("pant-icon.png", 100, 450, "pant-icon")
dressButton = Button("dress-icon.png", 100, 550, "dress-icon")
hat1Button = Button("earmuff.png", 250, 150, "earmuff")
hat2Button = Button("necklace.png", 350, 150, "necklace")
shirt1Button = Button("crop-top.png", 250, 250, "crop-top")
shirt2Button = Button("orange-shirt.png", 350, 250, "orange-shirt")
shirt3Button = Button("pink-sweater.png", 450, 250, "pink-sweater")
shoe1Button = Button("boots.png", 250, 350, "boots")
shoe2Button = Button("grey-shoes.png", 350, 350, "grey-shoes")
pants1Button = Button("jeans.png", 250, 450, "jeans")
pants2Button = Button("red-skirt.png", 350, 450, "red skirt")
dress1Button = Button("overalls.png", 250, 550, "overalls")
dress2Button = Button("purple-dress.png", 350, 550, "purpledress")
hats = [hat1Button, hat2Button]
shirts = [shirt1Button, shirt2Button, shirt3Button]
shoes = [shoe1Button, shoe2Button]
pants = [pants1Button, pants2Button]
dresses = [dress1Button, dress2Button]
state = States.MENU
current = SubClothing.INITIAL


class StateMachine:
    def __init__(self):
        self.currentState = States.MENU

    def changeState(self, state):
        self.currentState = state

class SubClothingMachine:
    def __init__(self):
        self.currentState = SubClothing.INITIAL

    def setEnabled(self, current):
        self.currentState = current


stateMachine = StateMachine()
subclothing = SubClothingMachine()

hatButton.function = lambda: stateMachine.changeState(States.HAT)
shirtButton.function = lambda: stateMachine.changeState(States.SHIRTS)
shoeButton.function = lambda: stateMachine.changeState(States.SHOES)
pantButton.function = lambda: stateMachine.changeState(States.PANTS)
dressButton.function = lambda: stateMachine.changeState(States.DRESS)



hat1Button.function = lambda: subclothing.setEnabled(SubClothing.HAT1)
hat2Button.function = lambda: subclothing.setEnabled(SubClothing.HAT2)
shirt1Button.function = lambda: subclothing.setEnabled(SubClothing.SHIRTS1)
shirt2Button.function = lambda: subclothing.setEnabled(SubClothing.SHIRTS2)
shirt3Button.function = lambda: subclothing.setEnabled(SubClothing.SHIRTS3)
shoe1Button.function = lambda: subclothing.setEnabled(SubClothing.SHOE1)
shoe2Button.function = lambda: subclothing.setEnabled(SubClothing.SHOE2)
pants1Button.function = lambda: subclothing.setEnabled(SubClothing.PANTS1)
pants2Button.function = lambda: subclothing.setEnabled(SubClothing.PANTS2)
dress1Button.function = lambda: subclothing.setEnabled(SubClothing.DRESS1)
dress2Button.function = lambda: subclothing.setEnabled(SubClothing.DRESS2)
# for item in allClothingItems:
# if item.is_enabled: screen.blit(item.image, item.pos)

introscreen = True
while introscreen:
    screen.blit(bgdimage, (0, 0))
    pygame.display.flip()
    pygame.time.delay(int(1000 / 60))
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Exiting")
                introscreen = False

while running:
    print(stateMachine.currentState)

    screen.fill(background_color)
    screen.blit(title, (270, 25))
    screen.blit(pygame.transform.scale(pygame.image.load('drawings/alien-base.png').convert_alpha(), (380, 600)),
                [600, 200])
    screen.blit(hatButton.image, hatButton.pos)
    screen.blit(shirtButton.image, shirtButton.pos)
    screen.blit(shoeButton.image, shoeButton.pos)
    screen.blit(pantButton.image, pantButton.pos)
    screen.blit(dressButton.image, dressButton.pos)

    for event in pygame.event.get():
        hatButton.get_event(event)
        hat1Button.get_event(event)
        hat2Button.get_event(event)
        shirtButton.get_event(event)
        shirt1Button.get_event(event)
        shirt2Button.get_event(event)
        shirt3Button.get_event(event)
        shoeButton.get_event(event)
        shoe1Button.get_event(event)
        shoe2Button.get_event(event)
        pantButton.get_event(event)
        pants1Button.get_event(event)
        pants2Button.get_event(event)
        dressButton.get_event(event)
        dress1Button.get_event(event)
        dress2Button.get_event(event)
        if event.type == pygame.QUIT:
            running = False

    if stateMachine.currentState == States.MENU:
        pass

    elif stateMachine.currentState == States.HAT:
        for button in hats:
            screen.blit(button.image, button.pos)

        if subclothing.currentState == SubClothing.HAT1:
            screen.blit(hat1Button.image, (790, 220))
        elif subclothing.currentState == SubClothing.HAT2:
            screen.blit(hat2Button.image, (775, 350))
        else:
            subclothing.currentState == SubClothing.INITIAL
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
