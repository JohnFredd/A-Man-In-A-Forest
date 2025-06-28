import pygame
import os

class levelThumbnail(pygame.sprite.Sprite):
	def __init__(self, x, y, name, onclick=lambda: None):
		super().__init__()
		self.image = pygame.image.load(os.path.join("assets", name + ".png")).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topleft = (x,y)
		self.onclick = onclick
		self.pressed = False
	
	def handleEvent(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(pygame.mouse.get_pos()):
				self.pressed = True
		elif event.type == pygame.MOUSEBUTTONUP and self.pressed:
			self.pressed = False
			if self.rect.collidepoint(pygame.mouse.get_pos()):
				self.onclick()