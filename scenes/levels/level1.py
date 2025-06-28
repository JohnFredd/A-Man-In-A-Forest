from scenes.baseScene import BaseScene
from ui.background import Background
from entities.player import Player

class Level1(BaseScene):
	def __init__(self, sceneManager):
		super().__init__(sceneManager)
		self.sprites.add(Background("lvl1Background"))
		self.sprites.add(Player(self, sceneManager.screen.get_rect().center))
	
	def goMainMenu(self):
		self.sceneManager.changeScene("MainMenu")