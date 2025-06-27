from scenes.mainMenu import MainMenu
from scenes.lvlSelector import LvlSelector

class SceneManager:
	def __init__(self, game):
		self.screen = game.screen
		self.currentScene = MainMenu(self)
		self.scenes = {
			"MainMenu": MainMenu,
			"LvlSelector": LvlSelector,
		}

	def update(self, events):
		self.currentScene.update(events)

	def draw(self):
		self.currentScene.draw()
	
	def changeScene(self, nextScene):
		sceneClass = self.scenes.get(nextScene)
		if sceneClass:
			self.currentScene = sceneClass(self)