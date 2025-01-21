import pygame
class Player(pygame.sprite.Sprite):
    speed = 1
    health = 100
    image=""
    x = 0
    y = 0
    width = 100
    heigth = 100
    surface = ""
    rect = ""




    def __init__(self,  image, width=10, height=10, x=500, y=500):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.heigth = height
        self.surface = pygame.image.load(image)
        self.surface.set_colorkey((255,255,255))
        self.surface = pygame.transform.scale(self.surface, (width,height))
        self.rect = self.surface.get_rect(center=(self.x, self.y))    
    def drow(self,screen:pygame.Surface):
        self.rect.center = (self.x, self.y)
        screen.blit(self.surface, self.rect)
        