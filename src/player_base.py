

import pygame
from pygame.locals import *


class PlayerBase:
    def __init__(self, tela, borda, largura, altura):
        self.tela = tela
        self.borda = borda
        self.colisao = borda
        self.largura = largura
        self.altura = altura
        self.x = self.largura // 2 - 40 // 2
        self.y = self.altura // 2 - 5 // 2 + 100
        self.rect = pygame.Rect(self.x, self.y, 40, 5)

    def player_colisao(self):
        if self.x < self.borda.left:
            self.x = self.borda.left

        if self.x + 40 > self.borda.right:
            self.x = self.borda.right - 40

        self.rect.x = self.x

    def reset(self):
        self.x = self.largura // 2 - 40 // 2
        self.rect.x = self.x