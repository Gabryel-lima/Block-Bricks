import pygame
from pygame.locals import *
from sys import exit
import os
import random

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Block-Bricks')
        self.relogio = pygame.time.Clock()
        self.largura = 600
        self.altura = 600
        self.pontos = 0
        self.mesg = f'Pontos: {self.pontos}'
        self.fonte = pygame.font.SysFont('arial', 30, True, False)
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.borda = pygame.Rect(0, 0, self.largura, self.altura)
        self.player = Player(self, self.borda)
        self.bola = Bola(self)
        self.blocos = Blocos(self)
        self.jogo_iniciado = False

    def layout(self):
        self.tela.fill((0,0,0))
        if not self.jogo_iniciado:
            self.exibir_mensagem("Pressione 'Enter' para iniciar o jogo", (self.largura // 2, self.altura // 2))

        pygame.draw.circle(self.tela, (255,255,255), ((self.bola.x), (self.bola.y)), self.bola.raio)
        pygame.draw.rect(self.tela, (255,0,0), ((self.player.x), (self.player.y), 40, 5))
        pygame.draw.rect(self.tela, (115,115,115), self.borda, 3)
        
        self.blocos.desenhar_blocos()

    def exibir_mensagem(self, texto, posicao):
        fonte = pygame.font.Font(None, 30)
        mensagem = fonte.render(texto, True, (255,255,255))
        retangulo = mensagem.get_rect()
        retangulo.center = posicao
        self.tela.blit(mensagem, retangulo)

    def exibir_pontuacao(self):
        mensagem = self.mesg
        texto_formatado = self.fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (40,430))

    def mensagem_fim_de_jogo(self):
        if len(self.blocos.blocos) == 0 or self.bola.y + self.bola.raio >= self.altura - 180:
            texto_formatado = self.fonte.render(f'Fim de jogo!', False, (255,255,255))  
            self.tela.blit(texto_formatado, (215,225))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.blocos.resetar_blocos()
            self.reset()
            return
            
    def atualiza_pontuacao(self):
        self.pontos += 1
        self.mesg = f'Pontos: {self.pontos}'

    def reset_pontos(self):
        if self.jogo_iniciado == True:
            self.pontos = 0
            self.mesg = f'Pontos: {self.pontos}'

    def run(self):
        
        while True:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    os._exit(0)

                if not self.jogo_iniciado:
                    if event.type == KEYDOWN and event.key == K_RETURN:
                        self.jogo_iniciado = True
                        self.reset_pontos()
                        self.bola.iniciar_movimento()

            self.relogio.tick(60)
            self.layout()
            if self.jogo_iniciado:
                self.exibir_pontuacao()
                self.verificar_colisao()
                self.player.input_player()
                self.bola.atualizar()

            self.mensagem_fim_de_jogo()
            pygame.display.update()

    def verificar_colisao(self):
        if self.bola.rect.colliderect(self.player.rect):
            self.bola.inverter_direcao()
        
        for bloco in self.blocos.blocos:
            if self.bola.rect.colliderect(bloco):
                self.atualiza_pontuacao()
                self.bola.inverter_direcao()
                self.blocos.blocos.remove(bloco)
                break  # Adicionado para sair do loop após a colisão

    def reset(self):
        self.jogo_iniciado = False
        self.bola.reset()
        self.player.reset()

class TelaInicial:
        def __init__(self):
            pass

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
        self.rect = pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio * 1, self.raio * 1)

    def iniciar_movimento(self):
        self.velocidade_x = random.choice([-1,-2,-3,1,2,3])
        self.velocidade_y = random.choice([-3,-4,-5])
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
        self.velocidade_x *= 1

    def reset(self):
        self.x = 300
        self.y = 350
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.rect.center = (self.x, self.y)

class Blocos:
    def __init__(self, jogo):
        self.jogo = jogo
        self.num_fileiras = 4 #4
        self.num_blocos_por_fileira = 8 #8
        self.espaco_blocos = 16
        self.largura_bloco = (self.jogo.largura - (self.num_blocos_por_fileira + 1) * self.espaco_blocos) / self.num_blocos_por_fileira
        self.altura_bloco = 20
        self.blocos = []
        self.criar_blocos()

    def criar_blocos(self):
        for fileira in range(self.num_fileiras):
            for coluna in range(self.num_blocos_por_fileira):
                x = self.espaco_blocos + coluna * (self.largura_bloco + self.espaco_blocos)
                y = self.espaco_blocos + fileira * (self.altura_bloco + self.espaco_blocos)
                bloco = pygame.Rect(x, y, self.largura_bloco, self.altura_bloco)
                self.blocos.append(bloco)

    def desenhar_blocos(self):
        for bloco in self.blocos:
            pygame.draw.rect(self.jogo.tela, (100,100,100), bloco)

    def resetar_blocos(self):
        self.blocos.clear()
        self.criar_blocos()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()