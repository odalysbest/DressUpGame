from enum import Enum


def __init__(self, img, x, y, name):
    self.pos = [x, y]
    try:
        self.image = pygame.transform.scale(pygame.image.load(img).convert_alpha(), (100, 100))
    except:
        try:
            self.image = pygame.transform.scale(pygame.image.load('drawings/' + img).convert_alpha(), (100, 100))
        except:
            self.image = pygame.transform.scale(pygame.image.load('icons/' + img).convert_alpha(), (100, 100))
    self.rect = pygame.Rect(x, y, 100, 100)
    self.name = name
    self.function = lambda: None
    # self.newfunction = screen


self.pos = [x, y]
try:
    self.image = pygame.transform.scale(pygame.image.load(img).convert_alpha(), (200, 200))
except:
    try:
        self.image = pygame.transform.scale(pygame.image.load('resized-pics/' + img).convert_alpha(), (100, 100))

    except:
        try:
            self.image = pygame.transform.scale(pygame.image.load('icons/' + img).convert_alpha(), (100, 100))
        except:
            try:
                self.image = pygame.transform.scale(pygame.image.load('shirts' + img).convert_alpha(), (100, 100))
            except:
                try:
                    self.image = pygame.transform.scale(pygame.image.load('dresses' + img).convert_alpha(),
                                                        (100, 100))
                except:
                    try:
                        self.image = pygame.transform.scale(pygame.image.load('hats' + img).convert_alpha(),
                                                            (100, 100))
                    except:
                        try:
                            self.image = pygame.transform.scale(
                                pygame.image.load('pants' + img).convert_alpha(),
                                (100, 100))
                        except:
                            try:
                                self.image = pygame.transform.scale(
                                    pygame.image.load('shoes' + img).convert_alpha(),
                                    (100, 100))

self.rect = pygame.Rect(x, y, 100, 100)
self.name = name
self.function = lambda: None
# self.newfunction = screen


