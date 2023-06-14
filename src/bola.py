
import random

import pygame
from pygame.locals import *

class Bola:
    def __init__(self, jogo, tela):
        self.tela = tela
        self.jogo = jogo
        self.x = 300
        self.y = 350
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.raio = 5
        self.rect = pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio * 1, self.raio * 1)
        
    def desenho_bola(self):
        pygame.draw.circle(self.tela, (255,255,255), ((self.x), (self.y)), self.raio)

    def iniciar_movimento(self):
        self.velocidade_x = random.randint(-3,3) # random.randint(-3,3) 
        self.velocidade_y = random.choice([-2,-3,-4]) # random.choice([-2,-3,-4])
        self.rect.center = (self.x, self.y)

    def atualizar(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y
        self.rect.center = (self.x, self.y)

        if self.x - self.raio <= 0 or self.x + self.raio >= self.jogo.largura:
            self.velocidade_x *= -1

        if self.y - self.raio <= 0:
            self.velocidade_y *= -1      

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

    def inverter_direcaoB(self):
        self.velocidade_y *= -1
        self.velocidade_x *= 1

    def reset(self):
        self.x = 300
        self.y = 350
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.rect.center = (self.x, self.y)
