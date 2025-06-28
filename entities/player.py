import pygame
import os
from entities.sword import Sword

class Player(pygame.sprite.Sprite):
	def __init__(self, scene, position):
		super().__init__()
		self.scene = scene
		self.image = pygame.image.load(os.path.join("assets", "player.png")).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = position
		self.velocity = 1
		self.attackInfo = {"atacking": False, "startAttack": 0, "endAttack": 0, "attackDuration": 250, "attackColdown": 250}
		self.sword = None
	
	def handleEvent(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				self.attack("up")
			if event.key == pygame.K_DOWN:
				self.attack("down")
			if event.key == pygame.K_LEFT:
				self.attack("left")
			if event.key == pygame.K_RIGHT:
				self.attack("right")
	
	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.rect.y -= self.velocity
		if keys[pygame.K_s]:
			self.rect.y += self.velocity
		if keys[pygame.K_a]:
			self.rect.x -= self.velocity
		if keys[pygame.K_d]:
			self.rect.x += self.velocity
		
		self.clampToScreen()

		if self.attackInfo["atacking"]:
			if self.attackInfo["startAttack"] + self.attackInfo["attackDuration"] < pygame.time.get_ticks():
				self.attackInfo["atacking"] = False
				self.attackInfo["endAttack"] = pygame.time.get_ticks()
				self.sword.kill()
				self.sword = None
			else:
				self.sword.playerRect = self.rect
	
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
