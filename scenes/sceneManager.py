from scenes.mainMenu import MainMenu
from scenes.lvlSelector import LvlSelector
from scenes.levels.level1 import Level1
from scenes.levels.level2 import Level2
from scenes.levels.level3 import Level3
from scenes.gameOver import GameOver

class SceneManager:
	def __init__(self, game):
		self.screen = game.screen
		self.currentScene = MainMenu(self)
		self.scenes = {
			"MainMenu": MainMenu,
			"LvlSelector": LvlSelector,
			"Level1" : Level1,
			"Level2" : Level2,
			"Level3" : Level3,
			"GameOver" : GameOver
		}

	def update(self, events):
		self.currentScene.update(events)

	def draw(self):
		self.currentScene.draw()
	
	def changeScene(self, nextScene, **kwargs):
		sceneClass = self.scenes.get(nextScene)
		if sceneClass:
			self.currentScene = sceneClass(self, **kwargs)