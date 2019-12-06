import os, sys
import pygame
import numpy as np
from pygame.locals import *
from pathlib import Path


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

        #Randomly select file
        path = Path("Backgroundimages")
        files = os.listdir(path)
        index = random.randrange(0, len(files))
        #print(files[index])

        # Create The Backgound
        game = True
        self.screen.fill((0,0,0))
        background = newScreen(files[index], [0,0])
