from math import pi, cos, sin
from pygame import Color
from pygame.math import Vector2
from pygame.sprite import DirtySprite, Sprite
import pygame.draw


class Button(Sprite):

    def __init__(self, x, y):
        self.pos = [x, y]



    def draw(self, screen):
        raise NotImplementedError


class Shirt(Button):
    def __init__(self):
        super().__init__(x, y)
        self.pos = [x, y]


    def draw(self, screen):



class Pants(Button):
    def __init__(self):
        super().__init__(x, y)


    def draw(self, screen):

class Dress(Button):
    def __init__(self):
        super().__init__(x, y)


    def draw(self, screen):


class Shoes(Button):
    def __init__(self):
        super().__init__(x, y):

    def draw(self, screen):

class Accessory(Buttons):
    def __init__(self):
        super().__init__(x, y)

    def draw(self, screen):

