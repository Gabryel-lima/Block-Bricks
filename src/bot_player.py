
import pygame
from pygame.locals import *

from player import Player


class BotPlayer:
    def __init__(self):
        self.player = Player

    def bot_desenho_player(self):
        self.player.desenho_player()
        
    def bot_input_player(self):
        bot_inp = self.player.input_player()

    def bot_reset_1(self):
        self.player.resetp_1()