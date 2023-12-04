

import pygame
from pygame.locals import *

class PlayerBase:
    def __init__(self, config_button):
        self.config_button = config_button
        self.x = 280
        self.y = 402
        self.rect = pygame.Rect(self.x, self.y, 40, 1)

    def player_colisao(self):
        if self.x < self.config_button.borda.left:
            self.x = self.config_button.borda.left

        if self.x + 40 > self.config_button.borda.right:
            self.x = self.config_button.borda.right - 40

        self.rect.x = self.x

    def reset(self):
        self.x = self.config_button.largura // 2 - 40 // 2
        self.rect.x = self.x

