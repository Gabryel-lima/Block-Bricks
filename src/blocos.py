


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
        #self.init_lista_rand_blocos() # Inicia uma lista aleatória de blocos resistentes.
        #self.init_rand_dos_blocos_dict()

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

    def init_lista_rand_blocos(self):
        self.indice_aleatorio = random.sample(range(len(self.blocos)), self.countr)
        print('Init_lista_rand_blocos:', self.indice_aleatorio)
        pass
        

    def init_rand_dos_blocos_dict(self):
        self.count = 0
        self.nsort = {}  # Inicializa o dicionário self.nsort.
        for self.indice in self.indice_aleatorio:
            if self.indice < len(self.blocos):
                self.nsort[self.indice] = random.randint(0,2)
                self.blocos[self.indice] = self.nsort[self.indice]

                self.remove_bloco_indice()

                #print('Dicionario:', self.nsort)
                #print('Lista de Indice aleatório:', self.indice_aleatorio)
                #print('Indice interável com dicionário:', self.nsort[self.indice])
                #print('Rects:', self.blocos[self.indice])
                

    def remove_bloco_indice(self):
        if self.blocos[self.indice] == 0:
            self.blocos.remove(self.blocos[self.bloco])
            self.count += 1

            print(0)

        elif self.blocos[self.indice] == 1:
            self.count += 1
            self.blocos.remove(self.blocos[self.bloco])
            print(1)

        elif self.blocos[self.indice] == 2:
            self.count += 2
            self.blocos.remove(self.blocos[self.bloco])
            print(2)
        else:
            return self.count
        pass
        

    def resistencia_blocos(self):
        pass

    def resetar_blocos(self):
        self.blocos.clear()
        self.criar_blocos()