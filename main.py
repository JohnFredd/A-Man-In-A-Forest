import pygame
from config import Config
from scenes.sceneManager import SceneManager

class Game:
	def __init__(self):
		pygame.init()
		
		self.config = Config()
		self.running = True
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode(self.config.screenSize)
		self.sceneManager = SceneManager(self)

		pygame.display.set_caption(self.config.gameName)
	
	def runGame(self):
		while self.running:
			self.clock.tick(60)

			events = pygame.event.get()

			for event in events:
				if event.type == pygame.QUIT:
					self.running = False

			self.sceneManager.update(events)
			self.updateScreen()
	
	def updateScreen(self):
		self.screen.fill((0, 0, 0))
		self.sceneManager.draw()
		pygame.display.flip()

if __name__ == '__main__':
	game = Game()
	game.runGame()