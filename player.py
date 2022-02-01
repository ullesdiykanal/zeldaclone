import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
      super().__init__()
      self.image = pygame.image.load('../assets/test/player.png').convert_alpha()
      self.rect = self.image.get_rect(topleft = pos)