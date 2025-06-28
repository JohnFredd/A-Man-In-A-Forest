import pygame
import os

class Player(pygame.sprite.Sprite):
	def __init__(self, position):
		super().__init__()
		self.image = pygame.image.load(os.path.join("assets", "player.png")).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = position
		self.moving = {"up": False, "down": False, "left": False, "right": False}
		self.velocity = 1
	
	def handleEvent(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				self.moving["up"] = True
			if event.key == pygame.K_s:
				self.moving["down"] = True
			if event.key == pygame.K_a:
				self.moving["left"] = True
			if event.key == pygame.K_d:
				self.moving["right"] = True
		
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				self.moving["up"] = False
			if event.key == pygame.K_s:
				self.moving["down"] = False
			if event.key == pygame.K_a:
				self.moving["left"] = False
			if event.key == pygame.K_d:
				self.moving["right"] = False
	
	def update(self):
		if self.moving["up"]:
			self.rect.y -= self.velocity
		if self.moving["down"]:
			self.rect.y += self.velocity
		if self.moving["left"]:
			self.rect.x -= self.velocity
		if self.moving["right"]:
			self.rect.x += self.velocity