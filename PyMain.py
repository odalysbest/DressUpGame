import os, sys
import pygame
import numpy as np
from pygame.locals import *


class PyManMain:
    """The Main PyMan Class – This class handles the main
    initialization and creating of the Game."""

    def __init__(self, width=1000,height=1000):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Alien Dress Up')
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font_name = pygame.font.get_default_font()


    def game_intro(self):
        """"Create the Intro Screen"""

        intro = True
        self.screen.fill((0,0,0))
        titlescreen = newScreen('startscreen.png', [0,0])
        self.screen.blit(titlescreen.image,titlescreen.rect)
        pygame.display.flip()

        while intro:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                        if (event.key == K_SPACE):
                            # Press Space to Move to Next Screen
                            MainWindow.MainLoop()
        clock.tick(15)

    def MainLoop(self):
        """This is the Main Loop of the Game"""

        # Create The Backgound
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()

class newScreen(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
