import pygame
from pygame.locals import *
from sys import exit

class Jogo:
    def __init__(self):
        pygame.init()
        self.largura = 600
        self.altura = 600
        self.tela = pygame.display.set_mode((self.largura,self.altura))
        self.titulo = pygame.display.set_caption('Block-Bricks')
        self.relogio = pygame.time.Clock()

    def layout(self):
        self.borda = pygame.draw.rect(self.tela, (120, 150, 145), (0, 0, self.largura, self.altura), 3)

    def run(self):
        while True:

            self.relogio.tick(30)
            self.tela.fill('Black')
            self.layout()
            for event in pygame.event.get():
                if event. type == QUIT:
                    pygame.quit()
                    exit()
            
            pygame.display.update()

class Player:
    def __init__(self):
        pass

class Blocos:
    def __init__(self):
        pass

if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()