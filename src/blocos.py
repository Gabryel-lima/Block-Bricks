

import pygame
from pygame.locals import *

import random

class Blocos:
    def __init__(self, jogo):
        self.jogo = jogo
        self.nivel_atual = 0
        self.nsort = random.randint(0,3)
        self.countr = random.randint(2,12)
        self.indice_aleatorio = []
        self.niveis = [
            (8,2),  # nível 1: (num_colunas, num_blocos_por_fileira)
            (8,3),  # nível 2
            (8,4),  # nível 3
            (8,5),  # nível 4
            (8,6),  # nível 5
            (8,7),  # nível 6
            (8,7),  # nível 7
            (8,8),  # nível 8
            (8,8),  # nível 9
            (8,8)  # nível 10
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
            pygame.draw.rect(self.jogo.tela, (150,75,0), bloco, width=0, border_radius= 5)

    def resistencia_blocos(self):
        max_selecionados = min(self.countr, len(self.blocos))
        if max_selecionados >= len(self.blocos):
            max_selecionados = len(self.blocos) - 1
        
        self.indice_aleatorio = random.sample(range(len(self.blocos)), max_selecionados)
        print(self.indice_aleatorio)
        blocos_selecionados = [self.blocos[indice] for indice in self.indice_aleatorio]
        print(blocos_selecionados)

        self.blocos = [bloco for indice, bloco in enumerate(self.blocos) if indice not in self.indice_aleatorio]

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
            self.resistencia_blocos()

    def resetar_blocos(self):
        self.blocos.clear()
        self.nivel = 0
        self.criar_blocos()
        self.resistencia_blocos()
