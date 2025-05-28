from operator import truediv

import pygame

from Button import Button
from Enemy import Enemy
from Obstacle import Obstacle
from Player import Player
from map import mapOne


class Game:
    def __init__(self):
        self.menu_background = pygame.image.load('assets/menu_background.jpeg')
        self.playing = None
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Helvetica', 30)
        self.running = True



    def launch_menu(self):
        open = True
        title = self.font.render('Welcome', True, (0, 0, 0))
        start_button = Button(15, 45, 130, 70, (255, 255, 255), (255, 165, 0), 'Start', 30)

        title_rect = title.get_rect(x = 15, y = 15)
        while open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    open = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if start_button.is_button_pressed(mouse_pos, mouse_pressed):
                open = False
            self.window.blit(self.menu_background, (0, 0))
            self.window.blit(title, title_rect)
            self.window.blit(start_button.image, start_button.rect)
            self.clock.tick(52)
            pygame.display.update()


    def createMap(self):

        for i, row in enumerate(mapOne):
            for j, col in enumerate(row):
               if col == 'W':
                   Obstacle(self, j, i)
               if col == 'C':
                   self.player = Player(self, j, i)
               if col == 'G':
                   self.goblin = Enemy(self, j, i)
                   self.goblin.image.fill((0, 255, 0))
               if col == 'B':
                    self.blue = Enemy(self, j, i)
                    self.blue.image.fill((0, 0, 255))
               if col == 'O':
                   self.blue = Enemy(self, j, i)
                   self.blue.image.fill((255, 0, 0))





    def new_game(self):

        self.playing = True
        self.sprites = pygame.sprite.LayeredUpdates()
        self.obstacles = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.createMap()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False


    def update(self):
        self.sprites.update()

    def draw(self):
        self.window.fill((0, 0, 0))
        self.sprites.draw(self.window)
        self.clock.tick(52)
        pygame.display.update()

    def main_loop(self):
        while self.playing:
            self.events()
            self.draw()
            self.update()
        self.running = False

    def game_over(self):
        self.running = False


