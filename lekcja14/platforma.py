import pygame

class floor:
    def __init__(self, startX, startY, color):
        self.x = startX
        self.y = startY

        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)