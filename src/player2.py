import pygame
from pygame.locals import *

from player_base import PlayerBase

class Player2(PlayerBase):
    def __init__(self, tela, borda, largura, altura):
        super().__init__(tela, borda, largura, altura)

    def desenho_player(self):
        pygame.draw.rect(self.tela, (60,255,10), ((self.x), (self.y), 40, 5))

    def input_player2(self):
        novo_x = self.x
        if pygame.key.get_pressed()[K_LEFT]:
            novo_x -= 3.5

            if pygame.key.get_pressed()[K_RSHIFT]:
                novo_x -= 4.5

        if pygame.key.get_pressed()[K_RIGHT]:
            novo_x += 3.5

            if pygame.key.get_pressed()[K_RSHIFT]:
                novo_x += 4.5

        if self.colisao.left <= novo_x <= self.colisao.right - 40:
            self.x = novo_x

        self.x = novo_x

    def reset(self):
        self.x = 600 // 2 - 5 // 2 + 20

    