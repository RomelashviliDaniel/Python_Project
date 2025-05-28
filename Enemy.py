import random

import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        self.screen = screen
        self._layer = 2
        self.x = x * 40
        self.y = y * 40
        self.groups = self.screen.sprites, self.screen.enemies
        self.lives = 1
        self.width = 40
        self.height = 40
        self.x_change = 0
        self.y_change = 0
        self.direction = random.choice(['left', 'right'])
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y

    def movement(self):
        if self.direction == 'left':
            self.x_change -= 3


        if self.direction == 'right':
            self.x_change += 3


    def detect_collision(self, direction):
        collision = pygame.sprite.spritecollide(self, self.screen.obstacles, False)
        if collision:
            if direction == 'left':
                self.direction = 'right'

            if direction == 'right':
                self.direction = 'left'

    def update(self):

        self.movement()
        self.rect.x += self.x_change
        self.detect_collision(self.direction)
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0

    def kill(self):
        self.rect.y = 1000
