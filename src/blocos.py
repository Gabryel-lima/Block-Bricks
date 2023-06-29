


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
        self.remove_blocos() # Inicia uma lista aleatória de blocos resistentes.
        #self.rand_dos_blocos_dict()

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
        
    def remove_blocos(self):
        self.count = 0
        self.nsort = {}
        self.indice_aleatorio = random.sample(range(len(self.blocos)), self.countr)

        for self.indice in self.indice_aleatorio:
            self.nsort[self.indice] = random.randint(0,2)
            self.blocos = self.nsort.items()
            print('lista_rand_blocos:', self.indice_aleatorio) 
            print('Lista dos blocos:', self.blocos)

    def resetar_blocos(self):
        self.blocos.clear()
        self.criar_blocos()