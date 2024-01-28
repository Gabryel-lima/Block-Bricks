

import pygame
from pygame.locals import *


from src.core.player_base import PlayerBase


class Player(PlayerBase):
    def __init__(self, jogo_base:object):
        super().__init__(jogo_base)

    def desenho_player(self):
        pygame.draw.rect(self.jogo_base.tela, (255,0,0), ((self._pos_x), (self._pos_y), self._largura_draw_x, 5))

    def input_player(self):
        novo_x = self._pos_x
        if pygame.key.get_pressed()[K_a]:
            novo_x -= 3.5

            if pygame.key.get_pressed()[K_LSHIFT]:
                novo_x -= 4.5

        if pygame.key.get_pressed()[K_d]:
            novo_x += 3.5

            if pygame.key.get_pressed()[K_LSHIFT]:
                novo_x += 4.5

        # if self.colisao.left <= novo_x <= self.colisao.right - 40:
        #     self._pos_x = novo_x

        self._pos_x = novo_x

    def resetp_1(self):
        self._pos_x = self.jogo_base.largura // 2 - 68
