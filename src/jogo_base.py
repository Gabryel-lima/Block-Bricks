
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
        self.altura_relativa_bola = 180
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.borda = pygame.Rect(0, 0, self.largura, self.altura)
        self.fonte = pygame.font.SysFont('arial', 30, True, False)
        self.rect_botao_player1 = pygame.Rect(240,170,120,40)
        self.rect_botao_player2 = pygame.Rect(240,230,120,40)
        self.rect_botao_voltar = pygame.Rect(40,300,85,30)
        self.rect_botao_sublinhar_mod_player = pygame.Rect(245,210,0,5)
        self.rect_botao_sublinhar_mod_player2 = pygame.Rect(245,270,0,5)
        self.rect_botao_sublinhar_clink = pygame.Rect(40,558,0,3)
        self.rect_botao_sublinhar_voltar = pygame.Rect(40,340,0,3)
        self.clink_rect = pygame.Rect(40,522,280,30)
        self.fonte = pygame.font.SysFont('arial', 30, True, False)
        self.config_button = ConfigButton(self)
        self.player = Player(self)
        self.player2 = Player2(self)
        self.bola = Bola(self)
        self.blocos = Blocos(self)
        #self.bot = BotPlayer(self.tela, self.config_button.largura, self.player.x, self.player.y)
        self.coleta = ColetaDados()
        self.modo_player1 = f'Player 1'
        self.modo_player2 = f'Player 2'
        self.blit_xy_player1 = (245,170)
        self.blit_xy_player2 = (245,230)
        self.fonte_impact = pygame.font.SysFont("impact", 28)
        self.cor_botao_subl = (250,250,250)
        self.back = f'Voltar'
        self.blit_xy_voltar = (40,300)
        self.mesgite_iniciar = f'Pressione a tecla "Enter" para iniciar'
        self.blit_xy_iniciar1 = (100,205)
        self.blit_xy_iniciar2 = (55,270)
        self.nivel = 1
        self.blit_xy_exibe_nivel = (40,480)
        self.mesg_nivel = f'Nivel: {self.nivel}'
        self.blit_xy_nivel = (200,220)
        self.pontos2 = 0
        self.blit_xy_mesg1_pontos = (40,430)
        self.blit_xy_mesg_bp1 = (40,530)
        self.blit_xy_mesg2_pontos = (40,430)
        self.mesg2 = f'Pontos: {self.pontos2}'
        self.blit_xy_mesg_bp2 = (40,530)
        self.lp2 = self.carregar_melhor_pontuacao2()
        self.mesg_bp2 = f'Melhor pontuação: {self.lp2}'
        self.blit_xy_clink = (40,520)
        self.modo_jogador = None

    def aplicar_resolucao(self, largura, altura):
        if (largura, altura) == (600,600):
            self.largura = 600
            self.altura = 600
            self.altura_relativa_bola = 180
            self.tela = pygame.display.set_mode((self.largura, self.altura))
            self.borda = pygame.Rect((0,0), (self.largura, self.altura))
            self.config_button.img_xy = (475,495)
            self.blit_xy_player1 = (245,170)
            self.blit_xy_player2 = (245,230)
            self.rect_botao_player1 = pygame.Rect(240,170,120,40)
            self.rect_botao_player2 = pygame.Rect(240,230,120,40)
            self.rect_botao_sublinhar_mod_player = pygame.Rect(245,210,0,5) 
            self.rect_botao_sublinhar_mod_player2 = pygame.Rect(245,270,0,5)
            self.rect_botao_voltar = pygame.Rect(40,300,85,30)
            self.rect_botao_sublinhar_voltar = pygame.Rect(40,340,0,3)
            self.rect_botao_sublinhar_clink = pygame.Rect(40,558,0,3)
            self.clink_rect = pygame.Rect(40,522,280,30)
            self.config_button.rect_resolucao_texto1 = pygame.Rect(240,170,120,40)
            self.config_button.rect_resolucao_texto2 = pygame.Rect(240,230,120,40)
            self.config_button.rect_resolucao_texto3 = pygame.Rect(240,290,120,40)
            self.config_button.list_rect_resolucao_texto = [self.config_button.rect_resolucao_texto1,
                                                            self.config_button.rect_resolucao_texto2,
                                                            self.config_button.rect_resolucao_texto3]
            self.blit_xy_voltar = (40,300)
            self.blit_xy_clink = (40,520)
            self.blit_xy_mesg1_pontos = (40,430)
            self.blit_xy_mesg_bp1 = (40,530)   
            self.blit_xy_exibe_nivel = (40,480)     
            self.blit_xy_mesg2_pontos = (40,430)
            self.blit_xy_mesg_bp2 = (40,530)
            self.config_button.rect_botao_config = pygame.Rect(474.5,494.0,53.0,53.0)
            #self.blocos.configurar_nivel()

        elif (largura,altura) == (800,800):
            self.largura = 800
            self.altura = 800
            self.altura_relativa_bola = 370
            self.tela = pygame.display.set_mode((self.largura, self.altura))
            self.borda = pygame.Rect((0,0), (self.largura, self.altura))
            self.blit_xy_player1 = (345,227)
            self.blit_xy_player2 = (345,303)
            self.rect_botao_player1 = pygame.Rect(320,227,160,53)
            self.rect_botao_player2 = pygame.Rect(320,307,160,53)
            self.rect_botao_sublinhar_mod_player = pygame.Rect(345,265,0,5)
            self.rect_botao_sublinhar_mod_player2 = pygame.Rect(345,345,0,5)
            self.rect_botao_voltar = pygame.Rect(40,400,85,30)
            self.blit_xy_voltar = (54,400)
            self.rect_botao_sublinhar_voltar = pygame.Rect(53,440,0,3)
            self.clink_rect = pygame.Rect(55,710,280,30)
            self.config_button.rect_resolucao_texto1 = pygame.Rect(320,277,120,40)
            self.config_button.rect_resolucao_texto2 = pygame.Rect(320,307,120,40)
            self.config_button.rect_resolucao_texto3 = pygame.Rect(320,337,120,40)
            self.config_button.list_rect_resolucao_texto = [self.config_button.rect_resolucao_texto1,
                                                            self.config_button.rect_resolucao_texto2,
                                                            self.config_button.rect_resolucao_texto3]
            self.blit_xy_clink = (55,710)
            self.blit_xy_mesg1_pontos = (40,600)
            self.blit_xy_mesg_bp1 = (40,650)
            self.blit_xy_exibe_nivel = (40,550)
            self.blit_xy_mesg2_pontos = (40,600)
            self.blit_xy_mesg_bp2 = (40,650)
            self.config_button.img_xy = (675,695)
            self.rect_botao_sublinhar_clink = pygame.Rect(55,750,0,5)
            self.config_button.rect_botao_config = pygame.Rect(674.5,694.0,53.0,53.0)
            self.blocos.configurar_nivel(16,57,20)

        #elif (largura,altura) == (FULLSCREEN): FUTURA RESOLUÇÃO DE TELA CHEIA.

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
        self.tela.blit(texo_formatado, self.blit_xy_mesg_bp2)
    
    def exibir_pontuacao2(self):
        mensagem = self.mesg2
        texto_formatado = self.fontei.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, self.blit_xy_mesg2_pontos)

    def atualiza_pontuacao2(self):
        self.pontos2 += 1
        self.mesg2 = f'Pontos: {self.pontos2}'

    def exibir_mensagem_inte_iniciar(self):
        mensagem = self.mesgite_iniciar
        fonte = pygame.font.SysFont('times new roman', 25, True, False)
        texto_formatado = fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, self.blit_xy_iniciar1)
        mensagem = self.mesgc
        fonte = pygame.font.SysFont('colibri', 30, False, False)
        texto_formatado = fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (60,240))
        if self.modo_jogador == 'Player2':
            mensagem = self.mesgc2
            fonte = pygame.font.SysFont('colibri', 30, False, False)
            texto_formatado = fonte.render(mensagem, False, (255,255,255))  
            self.tela.blit(texto_formatado, self.blit_xy_iniciar2)
            self.player2.desenho_player()

    def desenho_borda(self):
        pygame.draw.rect(self.tela, (115,115,115), self.borda, 3)

    def animaçao_de_sublinhar_botao_tela_inicial(self):
        pygame.draw.rect(self.tela, self.cor_botao_subl, self.rect_botao_sublinhar_mod_player)
        pygame.draw.rect(self.tela, self.cor_botao_subl, self.rect_botao_sublinhar_mod_player2)
        pygame.draw.rect(self.tela, self.cor_botao_subl, self.rect_botao_sublinhar_clink)

        self.rect_botao_sublinhar_mod_player.width = min(self.rect_botao_sublinhar_mod_player.width, 110)
        self.rect_botao_sublinhar_mod_player.width = max(self.rect_botao_sublinhar_mod_player.width, 0)
        self.rect_botao_sublinhar_mod_player2.width = min(self.rect_botao_sublinhar_mod_player2.width, 113)
        self.rect_botao_sublinhar_mod_player2.width = max(self.rect_botao_sublinhar_mod_player2.width, 0)
        self.rect_botao_sublinhar_clink.width = min(self.rect_botao_sublinhar_clink.width, 3)
        self.rect_botao_sublinhar_clink.width = max(self.rect_botao_sublinhar_clink.width, 0)

    def botoes_tela_inicial_modos(self): # As condições aqui nunca param de rodar, melhoria futura...
        pos_mouse = pygame.mouse.get_pos()
        mod1 = self.modo_player1
        mod2 = self.modo_player2
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
            self.tela.blit(texto_formatado1, self.blit_xy_player1)
            texto_formatado2 = self.fonte.render(mod2, False, self.cor_botao_modo2)
            self.tela.blit(texto_formatado2, self.blit_xy_player2)
            
            self.config_button.botao_config()
            self.animaçao_de_sublinhar_botao_tela_inicial()

            texto_clink = 'Criado por: Gabryel-lima'
            texto_formatado_c = self.fonte_impact.render(texto_clink, False, self.cor_clink)
            self.tela.blit(texto_formatado_c, self.blit_xy_clink)

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
            self.tela.blit(texto_formatado1, self.blit_xy_voltar)

            self.animaçao_de_sublinhar_botao_voltar()

        return rect_botao
    
    def executar_particao_desenho_botoes_resolucao(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    os._exit(0)

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    rect1, rect2, rect3 = self.config_button.particao_desenho_botoes_resolucao()

                    if rect1.collidepoint(pygame.mouse.get_pos()):
                        self.aplicar_resolucao(600,600)
                        return
                    elif rect2.collidepoint(pygame.mouse.get_pos()):
                        self.aplicar_resolucao(800,800)
                        return
                    elif rect3.collidepoint(pygame.mouse.get_pos()):
                        self.aplicar_resolucao(*pygame.display.list_modes()[0])  # Obtém a maior resolução suportada
                        return
                else:
                    self.tela.fill((0,0,0))
                    self.desenho_borda()
                    self.config_button.particao_desenho_botoes_resolucao()
                    pygame.display.update()

    # def executar_particao_config(self):
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == QUIT:
    #                 pygame.quit()
    #                 os._exit(0)

    #             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    #                 if self.config_button.particao_desenho_botoes_resolucao():
    #                     print("Ué, mais isso não é coisa de mulher?")
    #                     #return
    #             else:
    #                 self.tela.fill((0,0,0))
    #                 self.desenho_borda()
    #                 self.config_button.particao_desenho_botoes_resolucao()
    #                 pygame.display.update()

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
                    pygame.time.delay(300)
                    #self.config_button.alterna_tela_inicial(limpar=True)
                    #self.executar_particao_config()
                    #self.config_button.alterna_tela_inicial(limpar=False)
                    self.executar_particao_desenho_botoes_resolucao()

    def executar_particao(self, particao=None):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    os._exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.desenho_botao_back().collidepoint(pygame.mouse.get_pos()):
                        self.reset()
                        self.tela.fill((0,0,0))
                        pygame.time.delay(300)
                        return 

                if event.type == KEYDOWN and event.key == K_RETURN:
                    self.jogo_iniciado = True
                    self.bola.iniciar_movimento()
                    if self.modo_jogador == "Player1":
                        #self.player.rect = Rect(0,0,0,0)
                        self.player.reset()
                        self.player2.rect = Rect(0,0,0,0)
                        self.tela.fill((0,0,0))
                        return
                    
                    elif self.modo_jogador == "Player2":
                        self.player.resetp_1()
                        #self.bot.bot_reset_1()
                        self.player2.reset()
                        self.player2.rect = Rect(self.player2.x, self.player2.y, 40, 1)
                        self.tela.fill((0,0,0))
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

