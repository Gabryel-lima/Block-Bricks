import pygame
from pygame.locals import *
from sys import exit
import random

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
        self.fonte = pygame.font.SysFont('arial', 30, True, False)
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.borda = pygame.Rect(0, 0, self.largura, self.altura)
        self.player = Player(self, self.borda)
        self.bola = Bola(self)
        self.blocos = Blocos(self)
        self.jogo_iniciado = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if not self.jogo_iniciado:
                    if event.type == KEYDOWN and event.key == K_RETURN:
                        self.jogo_iniciado = True
                        self.bola.iniciar_movimento()

            self.relogio.tick(60)
            self.layout()
            if self.jogo_iniciado:
                self.player.input_player()
                self.player.player_colisao()
                self.bola.atualizar()
                self.verificar_colisao()

            pygame.display.update()

    def layout(self):
        self.tela.fill((0,0,0))
        if not self.jogo_iniciado:
            self.exibir_mensagem("Pressione Enter para iniciar o jogo", (self.largura // 2, self.altura // 2))

        pygame.draw.circle(self.tela, (255, 255, 255), ((self.bola.x), (self.bola.y)), self.bola.raio)
        pygame.draw.rect(self.tela, (255, 0, 0), ((self.player.x), (self.player.y), 40, 5))
        pygame.draw.rect(self.tela, (120, 150, 145), self.borda, 3)

    def exibir_mensagem(self, texto, posicao):
        fonte = pygame.font.Font(None, 30)
        mensagem = fonte.render(texto, True, (255, 255, 255))
        retangulo = mensagem.get_rect()
        retangulo.center = posicao
        self.tela.blit(mensagem, retangulo)

    def verificar_colisao(self):
        if self.bola.rect.colliderect(self.player.rect):
            self.bola.inverter_direcao()
        elif self.bola.y + self.bola.raio >= self.altura - 190:
            self.reset()

    def reset(self):
        self.jogo_iniciado = False
        self.bola.reset()
        self.player.reset()

class Player:
    def __init__(self, jogo, borda):
        self.jogo = jogo
        self.colisao = borda
        self.x = self.jogo.largura // 2 - 40 // 2
        self.y = self.jogo.altura // 2 - 5 // 2 + 100
        self.rect = pygame.Rect(self.x, self.y, 40, 5)

    def input_player(self):
        novo_x = self.x
        if pygame.key.get_pressed()[K_a]:
            novo_x -= 3.5

        if pygame.key.get_pressed()[K_d]:
            novo_x += 3.5

        if self.colisao.left <= novo_x <= self.colisao.right - 40:
            self.x = novo_x

        self.rect.x = self.x

    def player_colisao(self):
        if self.x < self.jogo.borda.left:
            self.x = self.jogo.borda.left

        if self.x + 40 > self.jogo.borda.right:
            self.x = self.jogo.borda.right - 40

        self.rect.x = self.x

    def reset(self):
        self.x = self.jogo.largura // 2 - 40 // 2
        self.rect.x = self.x

class Bola:
    def __init__(self, jogo):
        self.jogo = jogo
        self.x = 300
        self.y = 350
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.raio = 5
        self.rect = pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio * 2, self.raio * 2)

    def iniciar_movimento(self):
        self.velocidade_x = random.choice([1,2,3,4])
        self.velocidade_y = -1
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
        self.velocidade_y *= -1

    def reset(self):
        self.x = 300
        self.y = 350
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.rect.center = (self.x, self.y)

class Blocos:
    def __init__(self, jogo):
        self.jogo = jogo

if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()

