import pygame




class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        self.screen = screen
        self.groups = self.screen.sprites
        self._layer = 2
        self.lives = 3
        self.speed = 5
        self.x = x * 40
        self.y = y * 40
        self.x_speed = 0
        self.y_speed = 0
        self.width = 40
        self.height = 40
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((150, 215, 55))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.moving_character()
        self.rect.x += self.x_speed
        self.detect_collision('x')
        self.rect.y += self.y_speed
        self.detect_collision('y')
        self.x_speed = 0
        self.y_speed = 0

    def detect_collision(self, movement_direction):
        object_collision = pygame.sprite.spritecollide(self, self.screen.obstacles, False)
        if object_collision:
            if movement_direction == 'x':
                if self.x_speed > 0:
                    self.rect.x = object_collision[0].rect.x - self.rect.width
                if self.x_speed < 0:
                    self.rect.x = object_collision[0].rect.x + self.rect.width
            if movement_direction == 'y':
                if self.y_speed > 0:
                    self.rect.y = object_collision[0].rect.y - self.rect.height
                if self.y_speed < 0:
                    self.rect.y = object_collision[0].rect.y + self.rect.height


   






    def moving_character(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.x_speed -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.x_speed += self.speed
        if keys_pressed[pygame.K_UP]:
            self.y_speed -= self.speed
        if keys_pressed[pygame.K_DOWN]:
            self.y_speed += self.speed
        if self.rect.x >= 800:
            for sprite in self.screen.sprites:
                sprite.rect.x -= 800
        if self.rect.x <= 0:
            for sprite in self.screen.sprites:
                sprite.rect.x += 800


    def set_x(self, x):
        self.rect.x = x
    def set_y(self, y):
        self.rect.y = y
