
import json
import os
import webbrowser

import pygame
from pygame.locals import *

from player import Player
from player2 import Player2
from bola import Bola
from blocos import Blocos
from config_button import ConfigButton
from coleta_dados import ColetaDados
from bot_player import BotPlayer


class JogoBase:
    def __init__(self):
        pygame.init()
        self.largura = 600
        self.altura = 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.borda = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect_botao_sublinhar_mod_player = pygame.Rect(240,210,0,5) #(240,210,0,5) #240,170,120,40
        self.rect_botao_sublinhar_mod_player2 = pygame.Rect(240,270,0,5)
        self.rect_botao_sublinhar_clink = pygame.Rect(40,558,0,3)
        self.rect_botao_sublinhar_voltar = pygame.Rect(40,340,0,3) 
        self.clink_rect = pygame.Rect(40,522,280,30)
        self.rect_botao_player1 = pygame.Rect(240,170,120,40)
        self.rect_botao_player2 = pygame.Rect(240,230,120,40)
        self.rect_botao_voltar = pygame.Rect(40,300,85,30)
        self.rect_botao_config = pygame.Rect(50,50,50,50)
        self.fonte = pygame.font.SysFont('arial', 30, True, False)
        self.player = Player(self.tela, self.borda, self.largura, self.altura)
        self.player2 = Player2(self.tela, self.borda, self.largura, self.altura)
        self.bola = Bola(self, self.tela, self.borda, self.largura, self.altura)
        self.blocos = Blocos(self)
        self.config_button = ConfigButton(self, self.rect_botao_player1)
        #self.bot = BotPlayer(self.tela, self.largura, self.player.x, self.player.y)
        self.coleta = ColetaDados()
        self.modo1 = f'Player 1'
        self.modo2 = f'Player 2'
        self.fonte_impact = pygame.font.SysFont("impact", 28)
        self.cor_botao_subl = (250,250,250)
        self.back = f'Voltar'
        self.mesgite = f'Pressione a tecla "Enter" para iniciar'
        self.nivel = 1
        self.mesg_nivel = f'Nivel: {self.nivel}'
        self.pontos2 = 0
        self.mesg2 = f'Pontos: {self.pontos2}'
        self.lp2 = self.carregar_melhor_pontuacao2()
        self.mesg_bp2 = f'Melhor pontuação: {self.lp2}'
        self.modo_jogador = None

    def carregar_melhor_pontuacao2(self):
        try:
            with open('src/best_score2.json', 'r') as file:
                data = json.load(file)
                return data['best_score2']
        except (FileNotFoundError, KeyError):
            return 0

    def salvar_melhor_pontuacao2(self):
        data = {'best_score2': self.lp2}
        with open('src/best_score2.json', 'w') as file:
            json.dump(data, file)

    def atualiza_melhor_pontuacao2(self):
        if self.pontos2 > self.lp2:
            self.lp2 = self.pontos2
            self.salvar_melhor_pontuacao2()
            self.mesg_bp2 = f'Melhor pontuação: {self.lp2}'

    def exibe_melhor_pontuacao2(self):
        mensagem = self.mesg_bp2
        texo_formatado = self.fontei.render(mensagem, False, (255,255,255))
        self.tela.blit(texo_formatado, (40,530))
    
    def exibir_pontuacao2(self):
        mensagem = self.mesg2
        texto_formatado = self.fontei.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (40,430))

    def atualiza_pontuacao2(self):
        self.pontos2 += 1
        self.mesg2 = f'Pontos: {self.pontos2}'

    def exibir_mensagem_inte_iniciar(self):
        mensagem = self.mesgite
        fonte = pygame.font.SysFont('times new roman', 25, True, False)
        texto_formatado = fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (100,205))
        mensagem = self.mesgc
        fonte = pygame.font.SysFont('colibri', 30, False, False)
        texto_formatado = fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (60,240))
        if self.modo_jogador == 'Player2':
            mensagem = self.mesgc2
            fonte = pygame.font.SysFont('colibri', 30, False, False)
            texto_formatado = fonte.render(mensagem, False, (255,255,255))  
            self.tela.blit(texto_formatado, (55,270))
            self.player2.desenho_player()

    def desenho_borda(self):
        pygame.draw.rect(self.tela, (115,115,115), self.borda, 3)

    def animacao_borda_bola(self):
        pass

    def exibir_credito(self):
        mensagem = self.credito
        texto_formatado1 = self.fonte_impact.render(mensagem, False, (255,255,255))
        self.tela.blit(texto_formatado1, (40,520))

    def animaçao_de_sublinhar_botao_tela_inicial(self):
        pygame.draw.rect(self.tela, self.cor_botao_subl, self.rect_botao_sublinhar_mod_player)
        pygame.draw.rect(self.tela, self.cor_botao_subl, self.rect_botao_sublinhar_mod_player2)
        pygame.draw.rect(self.tela, self.cor_botao_subl, self.rect_botao_sublinhar_clink)

        self.rect_botao_sublinhar_mod_player.width = min(self.rect_botao_sublinhar_mod_player.width, 113)
        self.rect_botao_sublinhar_mod_player.width = max(self.rect_botao_sublinhar_mod_player.width, 0)
        self.rect_botao_sublinhar_mod_player2.width = min(self.rect_botao_sublinhar_mod_player2.width, 113)
        self.rect_botao_sublinhar_mod_player2.width = max(self.rect_botao_sublinhar_mod_player2.width, 0)
        self.rect_botao_sublinhar_clink.width = min(self.rect_botao_sublinhar_clink.width, 3)
        self.rect_botao_sublinhar_clink.width = max(self.rect_botao_sublinhar_clink.width, 0)

    def botoes_tela_inicial_modos(self): # As condições aqui nunca param de rodar, melhoria futura...
        pos_mouse = pygame.mouse.get_pos()
        mod1 = self.modo1
        mod2 = self.modo2
        rect_modo1 = self.rect_botao_player1
        rect_modo2 = self.rect_botao_player2
        rect_c = self.clink_rect

        if rect_modo1.collidepoint(pos_mouse):
            self.cor_botao_modo1 = (170,170,170)
            self.rect_botao_sublinhar_mod_player.width += 3  
        else:
            self.cor_botao_modo1 = (255,255,255)
            self.rect_botao_sublinhar_mod_player.width -= 2

        if rect_modo2.collidepoint(pos_mouse):
            self.cor_botao_modo2 = (170,170,170)
            self.rect_botao_sublinhar_mod_player2.width += 3  
        else:
            self.cor_botao_modo2 = (255,255,255)
            self.rect_botao_sublinhar_mod_player2.width -= 2  

        if rect_c.collidepoint(pos_mouse):
            self.cor_clink = (170,170,170)
            self.cor_botao_subl = (225,225,225)
            self.rect_botao_sublinhar_clink.width += 280  
        else:
            self.cor_clink = (255,255,255)
            self.cor_botao_subl = (225,225,225)
            self.rect_botao_sublinhar_clink.width -= 280 

        if self.rect_botao_player1.width > 0 and self.rect_botao_player2.width > 0 and self.clink_rect.width > 0:
            texto_formatado1 = self.fonte.render(mod1, False, self.cor_botao_modo1)
            self.tela.blit(texto_formatado1, (240,170))
            texto_formatado2 = self.fonte.render(mod2, False, self.cor_botao_modo2)
            self.tela.blit(texto_formatado2, (240,230))
            
            self.config_button.botao_config()
            self.animaçao_de_sublinhar_botao_tela_inicial()

            m = 'Criado por: Gabryel-lima'
            texto_formatado_c = self.fonte_impact.render(m, False, self.cor_clink)
            self.tela.blit(texto_formatado_c, (40,520))

    def animaçao_de_sublinhar_botao_voltar(self):
        pygame.draw.rect(self.tela, self.cor_botao_subl, self.rect_botao_sublinhar_voltar)

        self.rect_botao_sublinhar_voltar.width = min(self.rect_botao_sublinhar_voltar.width, 6)
        self.rect_botao_sublinhar_voltar.width = max(self.rect_botao_sublinhar_voltar.width, 0)

    def desenho_botao_back(self):
        pos_mouse = pygame.mouse.get_pos()
        rect_botao = self.rect_botao_voltar
        mensagem = self.back

        if rect_botao.collidepoint(pos_mouse):
            self.cor_botao_voltar = (150,150,150)
            self.cor_botao_subl = (200,200,200)
            self.rect_botao_sublinhar_voltar.width += 80 
        else:
            self.cor_botao_voltar = (255,255,255)
            self.cor_botao_subl = (200,200,200)
            self.rect_botao_sublinhar_voltar.width -= 80

        if self.rect_botao_voltar.width > 0:  
            texto_formatado1 = self.fonte.render(mensagem, False, self.cor_botao_voltar)
            self.tela.blit(texto_formatado1, (40,300))

            self.animaçao_de_sublinhar_botao_voltar()

        return rect_botao

    def selecao_de_modos_estrutura(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect_botao_player1.collidepoint(pygame.mouse.get_pos()):
                    self.rect_botao_player1 = pygame.Rect(0,0,0,0)
                    pygame.time.delay(300)
                    self.modo_jogador = "Player1"

                    self.executar_particao(self.selecao_de_modos_estrutura_particao)

                elif self.rect_botao_player2.collidepoint(pygame.mouse.get_pos()):
                    self.rect_botao_player2 = pygame.Rect(0,0,0,0)
                    pygame.time.delay(300)
                    self.modo_jogador = "Player2"
                    self.salvar_melhor_pontuacao2()

                    self.executar_particao(self.selecao_de_modos_estrutura_particao2)

                elif self.clink_rect.collidepoint(pygame.mouse.get_pos()):
                        webbrowser.open("https://github.com/Gabryel-lima")
                        pygame.time.delay(300)
                
                elif self.config_button.desenho_botao_config().collidepoint(pygame.mouse.get_pos()):
                    self.rect_botao_player1 = Rect(0,0,0,0)
                    self.rect_botao_player2 = Rect(0,0,0,0)
                    self.clink_rect = Rect(0,0,0,0)
                    self.rect_botao_config = Rect(0,0,0,0)
                    self.config_button.img_xy = (0,0)
                    self.config_button.img_config = pygame.Surface(self.config_button.img_config.get_size())
                    pygame.time.delay(300)

                    self.executar_particao(self.selecao_de_modos_config)

    def executar_particao(self, particao):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    os._exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.desenho_botao_back().collidepoint(pygame.mouse.get_pos()):
                        self.reset()
                        pygame.time.delay(300)
                        self.tela.fill((0,0,0))
                        return

                if event.type == KEYDOWN and event.key == K_RETURN:
                    self.jogo_iniciado = True
                    self.bola.iniciar_movimento()
                    if self.modo_jogador == "Player1":
                        #self.player.rect = Rect(0,0,0,0)
                        self.player.reset()
                        self.player2.rect = Rect(0,0,0,0)
                        return
                    
                    elif self.modo_jogador == "Player2":
                        self.player.resetp_1()
                        #self.bot.bot_reset_1()
                        self.player2.reset()
                        self.player2.rect = Rect(self.player2.x, self.player2.y, 40, 1)
                        return
                else:
                    self.tela.fill((0,0,0))
                    self.desenho_botao_back()
                    self.desenho_borda()
                    self.bola.desenho_bola()
                    self.blocos.desenhar_blocos()
                    self.exibir_mensagem_inte_iniciar()
                    particao()
                    pygame.display.update()

    def selecao_de_modos_estrutura_particao(self):
        self.player.desenho_player()
        #self.bot.bot_desenho_player()

    def selecao_de_modos_estrutura_particao2(self):
        self.player.x = 530 // 2 - 40 // 2
        self.player2.x = 600 // 2 - 5 // 2 + 20
        self.player.desenho_player()
        self.player2.desenho_player()

    def selecao_de_modos_config(self):
        pass

    def niveis_count(self):
        self.nivel += 1
        self.mesg_nivel = f'Nivel: {self.nivel}'
                
    def manipula_nivel(self):
        while True:
            self.blocos.configurar_nivel()
            break

    def continuar_prox_nivel(self):
        self.jogo_iniciado = True
        self.bola.iniciar_movimento()
        self.manipula_nivel()
        self.rect_botao_player1 = pygame.Rect(0,0,0,0)
        self.rect_botao_player2 = pygame.Rect(0,0,0,0)
        return

