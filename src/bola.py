
import random

import pygame
from pygame.locals import *
from coleta_dados import ColetaDados

class Bola:
    def __init__(self, jogo, tela, borda, largura, altura):
        self.tela = tela
        self.jogo = jogo
        self.coleta = ColetaDados(tela, borda, largura, altura)
        self.x = 300   # 300
        self.y = 350   # 350   
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.raio = 5
        self.rect = pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio, self.raio)
        self.x_anterior = self.x        ##
        self.y_anterior = self.y        ##
        
    def desenho_bola(self):
        pygame.draw.circle(self.tela, (255,255,255), ((self.x), (self.y)), self.raio)

    def iniciar_movimento(self):
        self.velocidade_x = random.randint(-3,3)  # random.randint(-3,3) 
        self.velocidade_y = random.choice([-3,-4]) # random.choice([-3,-4])
        self.rect.center = (self.x, self.y)

    def atualizar(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y
        self.rect.center = (self.x, self.y)

        if self.x - self.raio <= 0 or self.x + self.raio >= self.jogo.largura:
            self.velocidade_x *= -1

        if self.y - self.raio <= 0:
            self.velocidade_y *= -1

        """ self.coleta.coletar_dados(pos_x=self.x, pos_y=self.y)
        self.coleta.salva_dados() """

    def inverter_direcao(self):
        if pygame.key.get_pressed()[K_a]:
            self.velocidade_y *= -1
            self.velocidade_x -= 1

        elif pygame.key.get_pressed()[K_d]:
            self.velocidade_y *= -1
            self.velocidade_x += 1
        else:
            self.velocidade_y *= -1
            self.velocidade_x *= 1

    def inverter_direcao2(self):
        if pygame.key.get_pressed()[K_LEFT]:
            self.velocidade_y *= -1
            self.velocidade_x -= 1

        elif pygame.key.get_pressed()[K_RIGHT]:
            self.velocidade_y *= -1
            self.velocidade_x += 1
        else:
            self.velocidade_y *= -1
            self.velocidade_x *= 1

    def reset(self):
        self.x = 300
        self.y = 350
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.rect.center = (self.x, self.y)

"""     def velocidade_vetorial(self):
        if self.x > self.x_anterior:
            return 
        elif self.x < self.x_anterior:
            return
        else:
            return """
