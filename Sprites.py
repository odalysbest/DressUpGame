from math import pi, cos, sin
from pygame import Color
from pygame.math import Vector2
from pygame.sprite import DirtySprite, Sprite
import pygame.draw
#skirt: (125, 115)
#jean(140, 235)
#dress(140, 235)
#pink sweater(290, 350)


class Button(Sprite):

    def __init__(self, img, x, y, name):
        self.pos = [x, y]
        try:
            self.image = pygame.transform.scale(pygame.image.load(img).convert_alpha(), (125, 115))
        except:
            try:
                self.image = pygame.transform.scale(pygame.image.load('drawings/'+img).convert_alpha(), (140, 235))
            except:
                try:
                    self.image = pygame.transform.scale(pygame.image.load('icons/' + img).convert_alpha(), (100, 100))
                except:
                    try:
                        self.image = pygame.transform.scale(pygame.image.load('shirts/'+img).convert_alpha(), (200, 240))
                    except:
                        try:
                            self.image = pygame.transform.scale(pygame.image.load('sweater/'+img).convert_alpha(), (290, 340))
                        except:
                            try:
                                self.image = pygame.transform.scale(pygame.image.load('overalls/'+img).convert_alpha(), (100, 400))
                            except:
                                try:
                                    self.image = pygame.transform.scale(pygame.image.load('shoes/' + img).convert_alpha(), (140, 115))
                                except:
                                    self.image = pygame.transform.scale(pygame.image.load('hats/'+img).convert_alpha(), (80, 80))


        self.rect = pygame.Rect(x, y, 100, 100)
        self.name = name
        self.function = lambda: None
        #self.newfunction = screen


    def get_event(self, event):
        clock = 0
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
            print("hello")
            clock +=1
        #if event.type == pygame.MOUSEBUTTONDOWN and clock == 1:
            #self.doubleclick(event)
            #clock -= 1


    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.function()

   # def doubleclick(self, event):
        #if self.rect.collidepoint(event.pos):
            #self.newfunction()

    def draw(self, screen):
        raise NotImplementedError

