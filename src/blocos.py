

import pygame
from pygame.locals import *

import random

class Blocos:
    def __init__(self, jogo):
        self.jogo = jogo
        self.nivel_atual = 0
        self.niveis = [
            (8,4),  # nível 1: (num_colunas, num_blocos_por_fileira)
            (5,2),  # nível 2
            (5,9),  # nível 3
            (6,1),  # nível 4
            (3,2),  # nível 5
            (5,4),  # nível 6
            (4,3),  # nível 7
            (3,1),  # nível 8
            (1,5),  # nível 9
            (7,10)  # nível 10
        ]
        self.configurar_nivel()

    def criar_blocos(self):
        for fileira in range(self.num_blocos_por_fileira):
            for coluna in range(self.num_colunas):
                x = self.espaco_blocos + coluna * (self.largura_bloco + self.espaco_blocos)
                y = self.espaco_blocos + fileira * (self.altura_bloco + self.espaco_blocos)
                self.bloco = pygame.Rect(x, y, self.largura_bloco, self.altura_bloco)
                self.blocos.append(self.bloco)

    def desenhar_blocos(self):
        for bloco in self.blocos:
            pygame.draw.rect(self.jogo.tela, (100,100,100), bloco)

    def configurar_nivel(self):
        if self.nivel_atual < len(self.niveis):
            self.num_colunas, self.num_blocos_por_fileira = self.niveis[self.nivel_atual]
            self.espaco_blocos = 16
            self.largura_bloco = 57
            self.altura_bloco = 20
            self.countr = random.randint(2,18)
            self.blocos = []
            self.nivel_atual += 1
            self.criar_blocos()

    def resetar_blocos(self):
        self.blocos.clear()
        self.nivel = 0
        self.criar_blocos()
