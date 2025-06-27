from scenes.mainMenu import MainMenu

class SceneManager:
	def __init__(self, game):
		self.game = game
		self.currentScene = MainMenu(self)

	def update(self):
		self.currentScene.update()

	def draw(self):
		self.currentScene.draw(self.game.screen)
	
	def changeScene(self, nextScene):
		self.currentScene = nextScene