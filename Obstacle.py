import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        self.screen = screen
        self._layer = 1
        self.groups = self.screen.sprites, self.screen.obstacles
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * 40
        self.y = y * 40
        self.width = 40
        self.height = 40
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
