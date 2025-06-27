from scenes.mainMenu import MainMenu

class SceneManager:
	def __init__(self, game):
		self.screen = game.screen
		self.currentScene = MainMenu(self)

	def update(self, events):
		self.currentScene.update(events)

	def draw(self):
		self.currentScene.draw()
	
	def changeScene(self, nextScene):
		self.currentScene = nextScene