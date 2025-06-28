from scenes.baseScene import BaseScene
from ui.button import Button
from ui.label import Label

class MainMenu(BaseScene):
	def __init__(self, sceneManager):
		super().__init__(sceneManager, (40,130,170))
		self.sprites.add(Label(200, 300, 800, 100, "A Man In A Forest", 100))
		self.sprites.add(Button(475, 600, 250, 100, "Play", onclick=self.goLvlSelector))
		
	def goLvlSelector(self):
		self.sceneManager.changeScene("LvlSelector")