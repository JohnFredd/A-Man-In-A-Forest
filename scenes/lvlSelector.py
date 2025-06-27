import pygame
from scenes.baseScene import BaseScene
from utils.button import Button
from utils.label import Label

class LvlSelector(BaseScene):
	def __init__(self, sceneManager):
		super().__init__(sceneManager, (40,130,170))
		self.sprites.add(Label(200, 100, 800, 100, "Level Selector", 60))
		self.sprites.add(Button(50, 850, 250, 100, "Back", onclick=self.goMainMenu))
	
	def goMainMenu(self):
		self.sceneManager.changeScene("MainMenu")