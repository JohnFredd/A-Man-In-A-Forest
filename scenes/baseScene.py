import pygame

class BaseScene:
	def __init__(self, sceneManager, sceneColor=(0,0,0)):
		self.sceneManager = sceneManager
		self.sprites = pygame.sprite.Group()
		self.sceneColor = sceneColor

	def update(self, events):
		for event in events:
			for sprite in self.sprites:
				if hasattr(sprite, 'handleEvent'):
					sprite.handleEvent(event)
		
		for sprite in self.sprites:
			if hasattr(sprite, "update"):
				sprite.update()

	def draw(self):
		self.sceneManager.screen.fill(self.sceneColor)
		self.sprites.update()
		self.sprites.draw(self.sceneManager.screen)