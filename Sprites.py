from math import pi, cos, sin
from pygame import Color
from pygame.math import Vector2
from pygame.sprite import DirtySprite, Sprite
import pygame.draw


class Button(Sprite):

    def __init__(self, img, x, y, name):
        self.pos = [x, y]
        try:
            self.image = pygame.transform.scale(pygame.image.load(img).convert_alpha(), (100, 100))
        except:
            try:
                self.image = pygame.transform.scale(pygame.image.load('drawings/'+img).convert_alpha(), (100, 100))
            except:
                self.image = pygame.transform.scale(pygame.image.load('icons/' + img).convert_alpha(), (100, 100))
        self.rect = pygame.Rect(x, y, 100, 100)
        self.name = name
        self.function = lambda: None


    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)


    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.function()


    def draw(self, screen):
        raise NotImplementedError


class Shirt(Button):
    def __init__(self):
        super().__init__(x, y)
        self.image = self.image = pygame.image.load(shirts).convert_alpha()

    def draw(self, screen):
        pygame.draw.rect(self.image, color, [0, screen])
        pass


class Pants(Button):
    def __init__(self):
        super().__init__(x, y)
        self.image = self.image = pygame.image.load(pant).convert_alpha()

    def draw(self, screen):
        pygame.draw.rect(self.image, color, [0, screen])
        pass


class Dress(Button):
    def __init__(self):
        super().__init__(x, y)
        self.image = self.image = pygame.image.load(dresses).convert_alpha()

    def draw(self, screen):
        pygame.draw.rect(self.image, color, [0, screen])
        pass


class Shoes(Button):
    def __init__(self):
        super().__init__(x, y)
        self.image = self.image = pygame.image.load(shoe).convert_alpha()

    def draw(self, screen):
        pygame.draw.rect(self.image, color, [0, screen])
        pass


class Accessory(Button):
    def __init__(self):
        super().__init__(x, y)
        self.image = self.image = pygame.image.load(accessories).convert_alpha()

    def draw(self, screen):
        pygame.draw.rect(self.image, color, [0, screen])
        pass
