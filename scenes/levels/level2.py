from scenes.baseScene import BaseScene
from ui.button import Button
from ui.label import Label

class Level2(BaseScene):
	def __init__(self, sceneManager):
		super().__init__(sceneManager)
		self.sprites.add(Label(200, 300, 800, 100, "Not Implemented Yet", 100))
	
	def goMainMenu(self):
		self.sceneManager.changeScene("MainMenu")