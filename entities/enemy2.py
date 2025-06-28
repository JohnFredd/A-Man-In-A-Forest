import pygame
import os
import math
from entities.sword import Sword

class Enemy2(pygame.sprite.Sprite):
	def __init__(self, scene, position):
		super().__init__()
		self.scene = scene
		self.image = pygame.image.load(os.path.join("assets", "enemy2.png")).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = position
		self.velocity = 1
		self.lastdamage = 0
		self.life = 3
	
	def update(self):
		(playerx, playery) = self.scene.player.rect.center
		(selfx, selfy) = self.rect.center
		directionx = playerx - selfx
		directiony = playery - selfy
		(movementx, movementy) = self.adjustVelocity(directionx, directiony)
		
		self.rect.x += movementx
		self.rect.y += movementy
		
		self.clampToScreen()

		if self.rect.colliderect(self.scene.player.rect):
			self.scene.playerKilled()
	
	def adjustVelocity(self, x, y):
		velocity = math.sqrt(x**2 + y**2)
		factor = self.velocity / velocity
		return (x * factor, y * factor)
	
	def clampToScreen(self):
		self.rect.left = max(0, self.rect.left)
		self.rect.right = min(self.scene.sceneManager.screen.get_width(), self.rect.right)

		self.rect.top = max(0, self.rect.top)
		self.rect.bottom = min(self.scene.sceneManager.screen.get_height(), self.rect.bottom)
	
	def hit(self):
		if self.lastdamage + 300 < pygame.time.get_ticks():
			self.life -= 1
			self.lastdamage = pygame.time.get_ticks()

			if self.life == 0:
				self.scene.updateScore()
				self.kill()
