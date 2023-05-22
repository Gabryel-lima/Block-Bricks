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


'''Importações: Importei apenas os módulos necessários do pygame (pygame e pygame.locals) e o módulo exit do pacote sys.

Classe Jogo: Na inicialização da classe, adicionei a criação de um objeto pygame.Rect chamado borda que representa a borda da área do jogo. Removi a linha self.titulo e defini o título diretamente usando pygame.display.set_caption. Também adicionei um objeto pygame.time.Clock() chamado relogio para controlar a taxa de atualização do jogo.

Método run(): Adicionei uma chamada ao método layout() no início do loop principal do jogo. Em seguida, movi a criação dos objetos Player, Bola e Blocos para antes do loop principal. Isso evita que esses objetos sejam criados a cada iteração do loop.

Método layout(): Modifiquei esse método para desenhar o jogador e a bola com base nas coordenadas x e y dos respectivos objetos. Utilizei as propriedades self.player.x, self.player.y, self.bola.x e self.bola.y para obter as coordenadas atualizadas dos objetos. Os retângulos são desenhados usando pygame.draw.rect() e pygame.draw.circle().

Classe Player: Removi a linha que desenha o retângulo do jogador na inicialização da classe, pois agora o desenho é feito no método layout(). No método input_player(), atualizei as verificações de tecla pressionada para mover o jogador de forma mais suave, adicionando uma velocidade fracionada ao novo_x. Verifiquei se o novo valor de x está dentro dos limites da borda antes de atualizar a posição do jogador.

Classe Bola: No método atualizar(), atualizei a posição da bola com base nas velocidades velocidade_x e velocidade_y. Verifiquei se a bola atingiu as bordas da área do jogo e inverti a direção das velocidades quando necessário.'''

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Block-Bricks')
        self.relogio = pygame.time.Clock()
        self.largura = 600
        self.altura = 600
        self.x = self.largura // 2 - 40 // 2 
        self.y = self.altura // 2 - 5 // 2 + 100
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.borda = pygame.Rect(0, 0, self.largura, self.altura)
        self.player = Player(self, self.borda)
        self.bola = Bola(self)
        self.blocos = Blocos(self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            self.relogio.tick(60)
            self.layout()
            self.player.input_player()
            self.player.player_colisao()
            self.bola.atualizar()
            self.verificar_colisao()

            pygame.display.update()

    def layout(self):
        self.tela.fill((0,0,0))
        pygame.draw.circle(self.tela, (255,255,255), ((self.bola.x), (self.bola.y)), self.bola.raio)
        pygame.draw.rect(self.tela, (255,0,0), ((self.player.x), (self.player.y), 40, 5))
        pygame.draw.rect(self.tela, (120,150,145), self.borda, 3)

    def verificar_colisao(self):
        if self.bola.rect.colliderect(self.player.rect):
            self.bola.inverter_direcao()

class Player:
    def __init__(self, jogo, borda):
        self.jogo = jogo
        self.colisao = borda
        self.x = self.jogo.x
        self.y = self.jogo.y
        self.velocidade = 4  # Velocidade do jogador
        self.rect = pygame.Rect(self.x, self.y, 40, 5)

    def input_player(self):
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            self.x -= self.velocidade

        if keys[K_d]:
            self.x += self.velocidade

        if self.colisao.left <= self.x <= self.colisao.right - 40:
            self.jogo.x = self.x

        self.rect = pygame.Rect(self.jogo.x, self.jogo.y, 40, 5)

    def player_colisao(self):
        if self.x < self.jogo.borda.left:
            self.x = self.jogo.borda.left

        if self.x + 40 > self.jogo.borda.right:
            self.x = self.jogo.borda.right - 40

class Bola:
    def __init__(self, jogo):
        self.jogo = jogo
        self.x = 300
        self.y = 350
        self.velocidade_x = 2
        self.velocidade_y = -2
        self.raio = 5
        self.rect = pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio * 2, self.raio * 2)

    def atualizar(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y
        self.rect.center = (self.x, self.y)

        if self.x - self.raio <= 0 or self.x + self.raio >= self.jogo.largura:
            self.velocidade_x *= -1

        if self.y - self.raio <= 0 or self.y + self.raio >= self.jogo.altura:
            self.velocidade_y *= -1

    def inverter_direcao(self):
        self.velocidade_y *= -1

class Blocos:
    def __init__(self, jogo):
        self.jogo = jogo

if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()
