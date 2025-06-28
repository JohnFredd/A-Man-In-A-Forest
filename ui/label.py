import pygame

class Label(pygame.sprite.Sprite): 
	def __init__(self, x, y, width, height, text="", textSize=36, color=(255,255,255)):
		super().__init__()
		self.image = self.render(width, height, text, textSize, color)
		self.rect = pygame.Rect(x, y, width, height)

	def render(self, width, height, text, textSize, color):
		surface = pygame.Surface((width, height), pygame.SRCALPHA)
		font = pygame.font.Font(None, textSize)
		textRender = font.render(text, True, color)
		textRect = textRender.get_rect(center=(width // 2, height // 2))
		surface.blit(textRender, textRect)
		return surface