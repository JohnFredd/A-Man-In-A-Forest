from scenes.baseScene import BaseScene
from ui.levelThumbnail import levelThumbnail
from ui.button import Button
from ui.label import Label

class LvlSelector(BaseScene):
	def __init__(self, sceneManager):
		super().__init__(sceneManager, (40,130,170))
		self.sprites.add(Label(200, 100, 800, 100, "Level Selector", 60))
		self.sprites.add(Button(50, 850, 250, 100, "Back", onclick=self.goMainMenu))
		self.sprites.add(Label(100, 300, 256, 60, "Level 1", 60))
		self.sprites.add(Label(472, 300, 256, 60, "Level 2", 60))
		self.sprites.add(Label(844, 300, 256, 60, "Level 3", 60))
		self.sprites.add(levelThumbnail(100,400, "lvl1Thumbnail", self.goLvl1))
		self.sprites.add(levelThumbnail(472,400, "lvl2Thumbnail", self.goLvl2))
		self.sprites.add(levelThumbnail(844,400, "lvl3Thumbnail", self.goLvl3))
	
	def goMainMenu(self):
		self.sceneManager.changeScene("MainMenu")
	
	def goLvl1(self):
		self.sceneManager.changeScene("Level1")

	def goLvl2(self):
		self.sceneManager.changeScene("Level2")

	def goLvl3(self):
		self.sceneManager.changeScene("Level3")