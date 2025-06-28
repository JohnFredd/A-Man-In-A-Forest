import pygame
import random
from scenes.baseScene import BaseScene
from ui.background import Background
from ui.label import Label
from entities.player import Player
from entities.enemy1 import Enemy1

class Level1(BaseScene):
	def __init__(self, sceneManager):
		super().__init__(sceneManager)
		self.background = Background("lvl1Background")
		self.sprites.add(self.background)
		self.score = 0
		self.scoreLabel = Label(0, 0, 1200, 200, "Score: 0", 50, (0,0,0))
		self.sprites.add(self.scoreLabel)

		self.player = Player(self, sceneManager.screen.get_rect().center)
		self.sprites.add(self.player)

		self.enemies = [Enemy1(self, self.background.rect.midleft), Enemy1(self, self.background.rect.midright)]
		self.sprites.add(self.enemies)
		self.spawnEnemy = 7000
		self.lastEnemySpawned = 0
	
	def update(self, events):
		super().update(events)
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.goMainMenu()

		if self.lastEnemySpawned + self.spawnEnemy < pygame.time.get_ticks():
			posibilities = [self.background.rect.midtop, self.background.rect.midbottom, self.background.rect.midleft, self.background.rect.midright]
			election = random.choice(posibilities)
			newEnemy = Enemy1(self, election)
			self.enemies.append(newEnemy)
			self.sprites.add(newEnemy)
			self.lastEnemySpawned = pygame.time.get_ticks()
			self.spawnEnemy = self.spawnEnemy * 0.9
			if self.spawnEnemy < 500:
				self.spawnEnemy = 500

	
	def goMainMenu(self):
		self.sceneManager.changeScene("MainMenu")
	
	def playerKilled(self):
		self.goMainMenu()
	
	def updateScore(self):
		self.score += 100
		self.scoreLabel.image = self.scoreLabel.render(1200, 200, "Score: " + str(self.score), 50, (0,0,0))