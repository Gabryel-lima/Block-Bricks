
import os

import pygame
from pygame.locals import *

from player import Player
from player2 import Player2
from bola import Bola
from blocos import Blocos

class JogoBase:
    def __init__(self):
        pygame.init()
        self.largura = 600
        self.altura = 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.borda = pygame.Rect(0, 0, self.largura, self.altura)
        self.fonte = pygame.font.SysFont('arial', 30, True, False)
        self.player = Player(self.tela, self.borda, self.largura, self.altura)
        self.player2 = Player2(self.tela, self.borda, self.largura, self.altura)
        self.bola = Bola(self, self.tela)
        self.blocos = Blocos(self)
        self.modo1 = f'Player 1'
        self.modo2 = f'Player 2'
        self.rect_botao_player1 = pygame.Rect(240,170,120,40)
        self.rect_botao_player2 = pygame.Rect(240,230,120,40)
        self.rect_botao_voltar = pygame.Rect(40,300,85,30)
        self.back = f'Voltar'
        self.mesgite = f'Pressione a tecla "Enter" para iniciar'  

    def exibir_mensagem_inte_iniciar(self):
        mensagem = self.mesgite
        fonte = pygame.font.SysFont('times new roman', 25, True, False)
        texto_formatado = fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (100,205))
        mensagem = self.mesgc
        fonte = pygame.font.SysFont('colibri', 30, False, False)
        texto_formatado = fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (60,250))

    def desenho_borda(self):
        pygame.draw.rect(self.tela, (115,115,115), self.borda, 3)

    def botoes_tela_inicial_modos(self):
            pos_mouse = pygame.mouse.get_pos()
            mod1 = self.modo1
            mod2 = self.modo2
            rect_modo1 = self.rect_botao_player1
            rect_modo2 = self.rect_botao_player2

            if rect_modo1.collidepoint(pos_mouse):
                self.cor_botao_modo1 = (150,150,150) 
            else:
                self.cor_botao_modo1 = (255,255,255)  

            if rect_modo2.collidepoint(pos_mouse):
                self.cor_botao_modo2 = (150,150,150) 
            else:
                self.cor_botao_modo2 = (255,255,255)  

            if self.rect_botao_player1.width > 0 and self.rect_botao_player2.width > 0:  
                texto_formatado1 = self.fonte.render(mod1, False, self.cor_botao_modo1)
                self.tela.blit(texto_formatado1, (240,170))
                texto_formatado2 = self.fonte.render(mod2, False, self.cor_botao_modo2)
                self.tela.blit(texto_formatado2, (240,230))

    def desenho_botao_back(self):
        pos_mouse = pygame.mouse.get_pos()
        rect_botao = self.rect_botao_voltar
        mensagem = self.back

        if rect_botao.collidepoint(pos_mouse):
            self.cor_botao_voltar = (150,150,150) 
        else:
            self.cor_botao_voltar = (255,255,255) 

        if self.rect_botao_voltar.width > 0 and self.rect_botao_voltar.width > 0:  
            texto_formatado1 = self.fonte.render(mensagem, False, self.cor_botao_voltar)
            self.tela.blit(texto_formatado1, (40,300))

        return rect_botao

    def selecao_de_modos_estrutura(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                
                if self.rect_botao_player1.collidepoint(pos_mouse):
                    self.rect_botao_player1 = pygame.Rect(0,0,0,0)
                    pygame.time.delay(300)

                    self.selecao_de_modos_estrutura_particao()

                elif self.rect_botao_player2.collidepoint(pos_mouse):
                    self.rect_botao_player2 = pygame.Rect(0,0,0,0)
                    pygame.time.delay(300)

                    def estrutura_de_decisao():
        
                        self.selecao_de_modos_estrutura_particao()
                    

    def selecao_de_modos_estrutura_particao(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    os._exit(0)

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.desenho_botao_back().collidepoint(pygame.mouse.get_pos()):
                        self.reset() # Metodo Herdado.
                        pygame.time.delay(300)
                        return

                if event.type == KEYDOWN and event.key == K_RETURN:
                    self.jogo_iniciado = True
                    self.bola.iniciar_movimento()
                    return
                else:
                    self.tela.fill((0,0,0))
                    self.desenho_botao_back()
                    self.desenho_borda()
                    self.player.desenho_player()
                    #self.player2.desenho_player()
                    self.bola.desenho_bola()
                    self.blocos.desenhar_blocos()
                    self.exibir_mensagem_inte_iniciar()
                    pygame.display.update()

    def continuar_prox_nivel(self):
        self.jogo_iniciado = True
        self.bola.iniciar_movimento()
        self.rect_botao_player1 = pygame.Rect(0,0,0,0)
        self.rect_botao_player2 = pygame.Rect(0,0,0,0)
        return
