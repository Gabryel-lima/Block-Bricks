
import pygame
from pygame.locals import *

class Player:
    def __init__(self, jogo, borda, tela):
        self.tela = tela
        self.jogo = jogo
        self.colisao = borda
        self.x = self.jogo.largura // 2 - 40 // 2
        self.y = self.jogo.altura // 2 - 5 // 2 + 100
        self.rect = pygame.Rect(self.x, self.y, 40, 5)

    def desenho_player(self):
        pygame.draw.rect(self.tela, (255,0,0), ((self.x), (self.y), 40, 5))

    def input_player(self):
        novo_x = self.x
        if pygame.key.get_pressed()[K_a]:
            novo_x -= 3.5

            if pygame.key.get_pressed()[K_LSHIFT]:
                novo_x -= 5

        if pygame.key.get_pressed()[K_d]:
            novo_x += 3.5

            if pygame.key.get_pressed()[K_LSHIFT]:
                novo_x += 5

        if self.colisao.left <= novo_x <= self.colisao.right - 40:
            self.x = novo_x

        self.rect.x = self.x

    def player_colisao(self):
        if self.x < self.jogo.borda.left:
            self.x = self.jogo.borda.left

        if self.x + 40 > self.jogo.borda.right:
            self.x = self.jogo.borda.right - 40

        self.rect.x = self.x

    def reset(self):
        self.x = self.jogo.largura // 2 - 40 // 2
        self.rect.x = self.x
        