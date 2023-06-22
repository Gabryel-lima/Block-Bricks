


import pygame
from pygame.locals import *

import random

class Blocos:
    def __init__(self, jogo):
        self.jogo = jogo
        self.num_colunas = 4
        self.num_blocos_por_fileira = 8
        self.espaco_blocos = 16
        self.largura_bloco = 57
        self.altura_bloco = 20
        self.countr = random.randint(2,18)
        self.blocos = []
        self.criar_blocos()
        self.init_blocos_sequenciais() # Inicia uma lista aleatória de blocos resistentes.
        self.init_rand_dos_blocos()

    def criar_blocos(self):
        for fileira in range(self.num_colunas):
            for coluna in range(self.num_blocos_por_fileira):
                x = self.espaco_blocos + coluna * (self.largura_bloco + self.espaco_blocos)
                y = self.espaco_blocos + fileira * (self.altura_bloco + self.espaco_blocos)
                self.bloco = pygame.Rect(x, y, self.largura_bloco, self.altura_bloco)
                self.blocos.append(self.bloco)

    def desenhar_blocos(self):
        for bloco in self.blocos:
            pygame.draw.rect(self.jogo.tela, (100,100,100), bloco)

    def init_blocos_sequenciais(self):
        self.indice_aleatorio = random.sample(range(len(self.blocos)), self.countr)
        #print(self.indice_aleatorio)
        pass

    def init_rand_dos_blocos(self):
        self.nsort = {}  # Inicializa o dicionário self.nsort.
        for indice in self.indice_aleatorio:
            pass

    def resistencia_blocos(self):
        pass

    def resetar_blocos(self):
        self.blocos.clear()
        self.criar_blocos()