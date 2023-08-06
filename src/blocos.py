

import pygame
from pygame.locals import *

import random

class Blocos:
    def __init__(self, jogo):
        self.jogo = jogo
        self.nivel_1()

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

    def configurar_nivel(self, nivel):
        self.num_colunas = 4
        self.num_blocos_por_fileira = 8
        self.espaco_blocos = 16
        self.largura_bloco = 57
        self.altura_bloco = 20
        self.countr = random.randint(2, 18)
        self.blocos = []
        self.criar_blocos()

        if nivel == 2:
            self.num_colunas = 5
            self.num_blocos_por_fileira = 2
            self.criar_blocos()
        elif nivel == 3:
            self.num_colunas = 5
            self.num_blocos_por_fileira = 9
            self.criar_blocos()
        elif nivel == 4:
            self.num_colunas = 6
            self.num_blocos_por_fileira = 10
            self.criar_blocos()
        elif nivel == 5:
            self.num_colunas = 3
            self.num_blocos_por_fileira = 2
            self.criar_blocos()
        elif nivel == 6:
            self.num_colunas = 5
            self.num_blocos_por_fileira = 4
            self.criar_blocos()
        elif nivel == 7:
            self.num_colunas = 4
            self.num_blocos_por_fileira = 3
            self.criar_blocos()
        elif nivel == 8:
            self.num_colunas = 3
            self.num_blocos_por_fileira = 1
        elif nivel == 9:
            self.num_colunas = 1
            self.num_blocos_por_fileira = 5
            self.criar_blocos()
        elif nivel == 10:
            self.num_colunas = 7
            self.num_blocos_por_fileira = 10
            self.criar_blocos()

    def nivel_1(self):
        self.num_colunas = 1
        self.num_blocos_por_fileira = 1
        self.espaco_blocos = 16
        self.largura_bloco = 57
        self.altura_bloco = 20
        self.countr = random.randint(2,18)
        self.blocos = []
        self.criar_blocos()

    def nivel_2(self):
        self.num_colunas = 4
        self.num_blocos_por_fileira = 8
        self.espaco_blocos = 16
        self.largura_bloco = 57
        self.altura_bloco = 20
        self.countr = random.randint(2,18)
        self.blocos = []
        self.criar_blocos()

    def nivel_3(self): 
        self.num_colunas = 4
        self.num_blocos_por_fileira = 8
        self.espaco_blocos = 16
        self.largura_bloco = 57
        self.altura_bloco = 20
        self.countr = random.randint(2,18)
        self.blocos = []
        self.criar_blocos()

    def nivel_4(self):
        self.num_colunas = 4
        self.num_blocos_por_fileira = 8
        self.espaco_blocos = 16
        self.largura_bloco = 57
        self.altura_bloco = 20
        self.countr = random.randint(2,18)
        self.blocos = []
        self.criar_blocos()

    def nivel_5(self): 
        self.num_colunas = 4
        self.num_blocos_por_fileira = 8
        self.espaco_blocos = 16
        self.largura_bloco = 57
        self.altura_bloco = 20
        self.countr = random.randint(2,18)
        self.blocos = []
        self.criar_blocos()

    def nivel_6(self): 
        self.num_colunas = 4
        self.num_blocos_por_fileira = 8
        self.espaco_blocos = 16
        self.largura_bloco = 57
        self.altura_bloco = 20
        self.countr = random.randint(2,18)
        self.blocos = []
        self.criar_blocos()

    def nivel_7(self): 
        self.num_colunas = 4
        self.num_blocos_por_fileira = 8
        self.espaco_blocos = 16
        self.largura_bloco = 57
        self.altura_bloco = 20
        self.countr = random.randint(2,18)
        self.blocos = []
        self.criar_blocos()

    def nivel_8(self): 
        self.num_colunas = 4
        self.num_blocos_por_fileira = 8
        self.espaco_blocos = 16
        self.largura_bloco = 57
        self.altura_bloco = 20
        self.countr = random.randint(2,18)
        self.blocos = []
        self.criar_blocos()

    def nivel_9(self): 
        self.num_colunas = 4
        self.num_blocos_por_fileira = 8
        self.espaco_blocos = 16
        self.largura_bloco = 57
        self.altura_bloco = 20
        self.countr = random.randint(2,18)
        self.blocos = []
        self.criar_blocos()

    def nivel_10(self): 
        self.num_colunas = 4
        self.num_blocos_por_fileira = 8
        self.espaco_blocos = 16
        self.largura_bloco = 57
        self.altura_bloco = 20
        self.countr = random.randint(2,18)
        self.blocos = []
        self.criar_blocos()

    def resetar_blocos(self):
        self.blocos.clear()
        self.criar_blocos()
