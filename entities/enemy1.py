import pygame
import os
import math
from entities.sword import Sword

class Enemy1(pygame.sprite.Sprite):
	def __init__(self, scene, position):
		super().__init__()
		self.scene = scene
		self.image = pygame.image.load(os.path.join("assets", "enemy1.png")).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = position
		self.velocity = 1
	
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
	
	def attack(self, direction):
		if (not self.attackInfo["atacking"]) and (self.attackInfo["endAttack"] + self.attackInfo["attackColdown"] < pygame.time.get_ticks()):
			self.attackInfo["atacking"] = True
			self.attackInfo["startAttack"] = pygame.time.get_ticks()
			self.attackInfo["direction"] = direction

			self.sword = Sword(self.scene, self.rect, direction)
			self.scene.sprites.add(self.sword)
