from scenes.baseScene import BaseScene
from ui.button import Button
from ui.label import Label
from entities.player import Player

class Level1(BaseScene):
	def __init__(self, sceneManager):
		super().__init__(sceneManager)
		self.sprites.add(Player(sceneManager.screen.get_rect().center))
	
	def goMainMenu(self):
		self.sceneManager.changeScene("MainMenu")