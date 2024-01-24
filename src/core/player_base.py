

import pygame
from pygame.locals import *

class PlayerBase:
    def __init__(self, jogo_base:object):
        self.jogo_base = jogo_base
        self._pos_x = 280
        self._pos_y = 402
        self._largura_draw_x = 40
        self._altura_draw_y = 1
        self.rect = pygame.Rect(self._pos_x, self._pos_y, self._largura_draw_x, self._altura_draw_y)

    @property
    def posicao_x(self) -> int:
        return self._pos_x
    
    @posicao_x.setter
    def ajuste_posicao_x(self, novo_valor:int):
        self._pos_x = novo_valor
        self.rect.x = novo_valor

    @property
    def posicao_y(self) -> int:
        return self._pos_y
    
    @posicao_y.setter
    def ajuste_posicao_y(self, novo_valor:int):
        self._pos_y = novo_valor
        self.rect.y = novo_valor

    @property
    def largura_draw_x(self) -> int:
        return self._largura_draw_x
    
    @largura_draw_x.setter
    def ajuste_largura_draw_x(self, novo_valor:int):
        self._pos_y = novo_valor
        self.rect.y = novo_valor
    
    @property
    def altura_draw_y(self) -> int:
        return self._altura_draw_y
    
    @altura_draw_y.setter
    def ajuste_altura_draw_y(self, novo_valor:int):
        self._pos_y = novo_valor
        self.rect.y = novo_valor
    
    def player_colisao(self):
        if self._pos_x - 5 <= self.jogo_base.borda.left:
            self._pos_x = self.jogo_base.borda.left + 5

        if self._pos_x + 45 >= self.jogo_base.borda.right:
            self._pos_x = self.jogo_base.borda.right - 45

        self.rect.x = self._pos_x

    def reset(self):
        self._pos_x = self.jogo_base.largura / 2 - self._largura_draw_x / 2
        self.rect.x = self._pos_x


    
    

