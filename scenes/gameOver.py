from scenes.baseScene import BaseScene
from ui.button import Button
from ui.label import Label

class GameOver(BaseScene):
	def __init__(self, sceneManager, score=0):
		super().__init__(sceneManager)
		self.sprites.add(Label(200, 300, 800, 100, "Game Over", 100))
		self.sprites.add(Label(0, 450, 1200, 100, "Score: " + str(score), 60))
		self.sprites.add(Button(475, 600, 250, 100, "Return", onclick=self.goMainMenu))
		
	def goMainMenu(self):
		self.sceneManager.changeScene("MainMenu")