import pygame
from pygame.locals import *

from player_base import PlayerBase

class Player(PlayerBase):
    def __init__(self, tela, borda, largura, altura):
        super().__init__(tela, borda, largura, altura)

    def desenho_player(self):
        pygame.draw.rect(self.tela, (255,0,0), ((self.x), (self.y), 40, 5))

    def input_player(self):
        novo_x = self.x
        if pygame.key.get_pressed()[K_a]:
            novo_x -= 3.5

            if pygame.key.get_pressed()[K_LSHIFT]:
                novo_x -= 4.5

        if pygame.key.get_pressed()[K_d]:
            novo_x += 3.5

            if pygame.key.get_pressed()[K_LSHIFT]:
                novo_x += 4.5

        if self.colisao.left <= novo_x <= self.colisao.right - 40:
            self.x = novo_x

        self.x = novo_x

    def reset(self):
        self.x = 530 // 2 - 40 // 2
