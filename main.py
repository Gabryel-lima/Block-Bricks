import pygame
from pygame.locals import *
from sys import exit
#from random import randint

class Jogo:
    def __init__(self):
        pygame.init()
        self.largura = 600
        self.altura = 600
        self.x = self.largura / 2 - 40 / 2 
        self.y = self.altura / 2 - 5 / 2 + 100
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.titulo = pygame.display.set_caption('Block-Bricks')
        self.mover_player = True

    def layout(self):
        self.tela.fill('Black')
        self.relogio = pygame.time.Clock()
        self.borda = pygame.draw.rect(self.tela, (120,150,145), (0, 0, self.largura, self.altura), 3)

    def run(self):
        while True:
            self.layout()
            self.player = Player(self, self.borda)
            self.blocos = Blocos(self)
            self.bola = Bola(self)
 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
        
            self.player.input_player()
            self.player.Player_colisao()

            pygame.display.update()

class Player:
    def __init__(self, jogo, borda):
        self.jogo = jogo
        self.colisao = borda
        self.player = pygame.draw.rect(self.jogo.tela, (255,0,0), (self.jogo.x,self.jogo.y,40,5))

    def input_player(self):
        if pygame.key.get_pressed()[K_a]:
            self.jogo.x -= 0.4

        if pygame.key.get_pressed()[K_d]:
            self.jogo.x += 0.4

    def Player_colisao(self):
        if not self.player.colliderect(self.colisao):
            self.jogo.x = 0 

class Bola:
    def __init__(self, jogo):
        self.jogo = jogo
        pass

class Blocos:
    def __init__(self, jogo):
        self.jogo = jogo
        pass

if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()
