import pygame


class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.SysFont('Arial', fontsize)
        self.content = content
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fg = fg
        self.bg = bg
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(bg)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(centerx=self.width/2, centery=self.height/2)
        self.image.blit(self.text, self.text_rect)
    def is_button_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False