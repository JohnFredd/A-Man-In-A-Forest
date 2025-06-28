import pygame
import os

class Sword(pygame.sprite.Sprite):
	def __init__(self, scene, playerRect, direction):
		super().__init__()
		self.scene = scene
		self.direction = direction
		self.originalImage = pygame.image.load(os.path.join("assets", "Sword.png")).convert_alpha()
		self.rotateSword()
		self.rect = self.image.get_rect()
		self.playerRect = playerRect
		self.rect.center = playerRect.center
	
	def rotateSword(self):
		if self.direction == "up":
			self.image = self.originalImage
		elif self.direction == "down":
			self.image = pygame.transform.rotate(self.originalImage, 180)
		elif self.direction == "left":
			self.image = pygame.transform.rotate(self.originalImage, 90)
		elif self.direction == "right":
			self.image = pygame.transform.rotate(self.originalImage, -90)
	
	def update(self):
		if self.direction == "up":
			self.rect.midbottom = self.playerRect.midtop
		elif self.direction == "down":
			self.rect.midtop = self.playerRect.midbottom
		elif self.direction == "left":
			self.rect.midright = self.playerRect.midleft
		elif self.direction == "right":
			self.rect.midleft = self.playerRect.midright

		collided = pygame.sprite.spritecollide(self, self.scene.enemies, False)
		for enemy in collided:
			enemy.kill()