from scenes.baseScene import BaseScene
from ui.button import Button
from ui.label import Label

class Level2(BaseScene):
	def __init__(self, sceneManager):
		super().__init__(sceneManager)
	
	def goMainMenu(self):
		self.sceneManager.changeScene("MainMenu")