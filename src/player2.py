

import pygame
from pygame.locals import *

from jogo import Jogo
from player import Player

class Player2(Player,Jogo):
    def __init__(self, jogo, borda, tela):
        super().__init__(jogo, borda, tela)

    def desenho_player(self):
        pygame.draw.rect(self.tela, (0,255,0), ((self.x), (self.y), 40, 5))

    def input_player2(self):
        novo_x = self.x
        if pygame.key.get_pressed()[K_LEFT]:
            novo_x -= 3.5

            if pygame.key.get_pressed()[K_RSHIFT]:
                novo_x -= 5

        if pygame.key.get_pressed()[K_RIGHT]:
            novo_x += 3.5

            if pygame.key.get_pressed()[K_RSHIFT]:
                novo_x += 5

        if self.colisao.left <= novo_x <= self.colisao.right - 40:
            self.x = novo_x

        self.rect.x = self.x