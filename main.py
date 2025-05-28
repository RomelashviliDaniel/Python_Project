import sys

import pygame

from Game import Game

game = Game()
game.launch_menu()
game.new_game()
while game.running:
    game.main_loop()
    game.game_over()
pygame.quit()
sys.exit()



