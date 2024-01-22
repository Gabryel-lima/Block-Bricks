

import pygame
from pygame.locals import *


class PlayerBase:
    def __init__(self, jogo_base:object, x:int=280, y:int=402):
        self.jogo_base = jogo_base
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 40, 1)

    def player_colisao(self):
        if self.x < self.jogo_base.borda.left:
            self.x = self.jogo_base.borda.left

        if self.x + 40 > self.jogo_base.borda.right:
            self.x = self.jogo_base.borda.right - 40

        self.rect.x = self.x

    def reset(self):
        self.x = self.jogo_base.largura // 2 - 40 // 2
        self.rect.x = self.x

