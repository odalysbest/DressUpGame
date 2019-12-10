from enum import Enum
from random import random, randint, randrange
import os, sys
import pygame
from pygame import Color
from Sprites import Button

pygame.display.init()
pygame.font.init()
GREEN = (19, 255, 140)
GREY = (209, 210, 210)
WHITE = (254, 255, 255)
RED = (254, 0, 0)
PURPLE = (254, 0, 255)

screen = pygame.display.set_mode([1000, 1000])
alien_img = pygame.transform.scale(pygame.image.load('alien-base.png').convert_alpha(), (600, 605))

background_images = [pygame.transform.scale(pygame.image.load("babson.jpg").convert_alpha(), (1000, 1000)),
                     pygame.transform.scale(pygame.image.load("beach.jpg").convert_alpha(), (1000, 1000)),
                     pygame.transform.scale(pygame.image.load("nightclub2.jpg").convert_alpha(), (1000, 1000)),
                     pygame.transform.scale(pygame.image.load("olin.jpg").convert_alpha(), (1000, 1000)),
                     pygame.transform.scale(pygame.image.load("snow.jpg").convert_alpha(), (1000, 1000))]
index = randrange(0, len(background_images))
background = (background_images[index])
myfont = pygame.font.SysFont('sansserif', 90)
title = myfont.render('Alien Dress Up', False, PURPLE)


    # add other buttons


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


hatButton = Button("hat-icon.png", 100, 100, "hat-icon")
shirtButton = Button("shirt-icon.png", 100, 250, "shirt-icon")
shoeButton = Button("shoe-icon.png", 100, 400, "shoe-icon")
pantButton = Button("pant-icon.png", 100, 550, "pant-icon")
dressButton = Button("dress-icon.png", 100, 700, "dress-icon")
hat1Button = Button("earmuff.png", 190, 100, "earmuff")
hat2Button = Button("necklace.png", 250, 100, "necklace")
shirt1Button = Button("crop-top.png", 150, 150, "crop-top")
shirt2Button = Button("orange-shirt.png", 250, 150, "orange-shirt")
shirt3Button = Button("pink-sweater.png", 350, 150, "pink-sweater")
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


class StateMachine:
    def __init__(self):
        self.currentState = States.MENU

    def changeState(self, state):
        self.currentState = state


stateMachine = StateMachine()

hatButton.function = lambda: stateMachine.changeState(States.HAT)
shirtButton.function = lambda: stateMachine.changeState(States.SHIRTS)
shoeButton.function = lambda: stateMachine.changeState(States.SHOES)
pantButton.function = lambda: stateMachine.changeState(States.PANTS)
dressButton.function = lambda: stateMachine.changeState(States.DRESS)

enabledict = {hat1Button: False, hat2Button: False, shirt1Button: False, shirt2Button: False, shirt3Button: False,
              shoe1Button: False, shoe2Button: False, pants1Button: False, pants2Button: False, dress1Button: False,
              dress2Button: False}


def setEnabled(item):
    enabledict[item] = not enabledict[item]


posdict = {hat1Button: (790, 250), hat2Button: (780, 380), shirt1Button: (710, 330), shirt2Button: (710, 325),
           shirt3Button: (648, 278), shoe1Button: (715, 705), shoe2Button: (715, 720), pants1Button: (745, 480),
           pants2Button: (745, 485), dress1Button: (760, 380), dress2Button: (745, 383)}

hat1Button.function = lambda: setEnabled(hat1Button)
hat2Button.function = lambda: setEnabled(hat2Button)
shirt1Button.function = lambda: setEnabled(shirt1Button)
shirt2Button.function = lambda: setEnabled(shirt2Button)
shirt3Button.function = lambda: setEnabled(shirt3Button)
shoe1Button.function = lambda: setEnabled(shoe1Button)
shoe2Button.function = lambda: setEnabled(shoe2Button)
pants1Button.function = lambda: setEnabled(pants1Button)
pants2Button.function = lambda: setEnabled(pants2Button)
dress1Button.function = lambda: setEnabled(dress1Button)
dress2Button.function = lambda: setEnabled(dress2Button)

introscreen = True
while introscreen:
    screen.blit(bgdimage, (0, 0))
    pygame.display.flip()

    screen.fill((0, 0, 0))
    pygame.time.delay(int(1000 / 60))
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Exiting")
                introscreen = False


while running:
    print(stateMachine.currentState)
    screen.blit(background, (0,0))
    screen.blit(title, (270, 25))
    screen.blit(alien_img, (500, 220))
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

    for item in enabledict:
        if enabledict[item]:
            screen.blit(item.image, posdict[item])

    pygame.display.flip()
    pygame.time.delay(int(1000 / 60))

pygame.quit()
