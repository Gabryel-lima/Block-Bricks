import pygame
from pygame.locals import *
from sys import exit
#from random import randint

""" Na função Player_colisao(), a linha self.jogo.x = self.colisao.right - self.player.width é responsável por ajustar a posição do jogador caso ele ultrapasse a borda direita da tela.

Vamos analisar essa linha em detalhes:

self.jogo.x: É a posição atual do jogador no eixo x.
self.colisao.right: É a coordenada do lado direito da área delimitada pela borda.
self.player.width: É a largura do retângulo do jogador.
A expressão self.colisao.right - self.player.width calcula a posição máxima que o jogador pode ter sem ultrapassar a borda direita. Se o jogador estiver além dessa posição máxima, ou seja, se self.player.right for maior que self.colisao.right, a linha ajusta a posição self.jogo.x para que o jogador fique exatamente na borda direita.

Isso garante que o jogador não ultrapasse a borda direita e permaneça visível dentro da área delimitada pelas bordas. """

class Jogo:
    def __init__(self):
        pygame.init()
        self.largura = 600
        self.altura = 600
        self.x = self.largura / 2 - 40 / 2 
        self.y = self.altura / 2 - 5 / 2 + 100
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.titulo = pygame.display.set_caption('Block-Bricks')

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
        novo_x = self.jogo.x
        if pygame.key.get_pressed()[K_a]:
            novo_x -= 0.4

        if pygame.key.get_pressed()[K_d]:
            novo_x += 0.4

        if self.colisao.left <= novo_x <= self.colisao.right - self.player.width:
            self.jogo.x = novo_x

    def Player_colisao(self):
        if self.player.left < self.colisao.left:
            self.jogo.x = self.colisao.left

        if self.player.right > self.colisao.right:
            self.jogo.x = self.colisao.right - self.player.width

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
