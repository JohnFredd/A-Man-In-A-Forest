import pygame
import os

class Background(pygame.sprite.Sprite):
	def __init__(self, name):
		super().__init__()
		self.image = pygame.image.load(os.path.join("assets", name + ".png")).convert_alpha()
		self.rect = self.image.get_rect()