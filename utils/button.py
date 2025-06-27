import pygame

class Button(pygame.sprite.Sprite): 
	def __init__(self, x, y, width, height, text="", textSize=36, onclick=lambda: None):
		super().__init__()
		self.onclick = onclick
		self.imageNormal = self.render(width, height, text, textSize, (75,170,40))
		self.imagePressed = self.render(width, height, text, textSize, (180,110,30))
		self.image = self.imageNormal
		self.rect = pygame.Rect(x, y, width, height)
		self.pressed = False

	def render(self, width, height, text, textSize, color):
		surface = pygame.Surface((width, height))
		surface.fill(color)
		font = pygame.font.Font(None, textSize)
		textRender = font.render(text, True, (255, 255, 255))
		textRect = textRender.get_rect(center=(width // 2, height // 2))
		surface.blit(textRender, textRect)
		return surface
	
	def handleEvent(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(pygame.mouse.get_pos()):
				self.pressed = True
				self.image = self.imagePressed
		elif event.type == pygame.MOUSEBUTTONUP and self.pressed:
			self.pressed = False
			self.image = self.imageNormal
			if self.rect.collidepoint(pygame.mouse.get_pos()):
				self.onclick()