
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
from redimensionar import Redimensionar
from data.bot_ia import ColetaDados
from data.bot_player import BotPlayer


class JogoBase:
    def __init__(self):
        self.vars_dimenssoes_tela()
        self.vars_tela_inicial()
        self.vars_tela_config()
        self.vars_pre_start()
        self.config_button = ConfigButton(self)
        self.redimensionar = Redimensionar(self)
        self.player = Player(self)
        self.player2 = Player2(self)
        self.bola = Bola(self)
        self.blocos = Blocos(self)
        #self.bot = BotPlayer(self.tela, self.config_button.largura, self.player.x, self.player.y)
        #self.coleta = ColetaDados()
        self.modo_player1 = f'Player 1'
        self.modo_player2 = f'Player 2'
        self.fonte_impact = pygame.font.SysFont("impact", 28)
        self.cor_botao_subl = (250,250,250)
        self.back = f'Voltar'
        self.mesgite_iniciar = f'Pressione a tecla "Enter" para iniciar'
        self.nivel = 1
        self.mesg_nivel = f'Nivel: {self.nivel}'
        self.pontos2 = 0
        self.mesg2 = f'Pontos: {self.pontos2}'
        self.lp2 = self.carregar_melhor_pontuacao2()
        self.mesg_bp2 = f'Melhor pontuação: {self.lp2}'
        self.modo_jogador = None
    
    def vars_dimenssoes_tela(self):
        pygame.init()
        self.largura = 600
        self.altura = 600
        self.altura_relativa_bola = 180
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.borda = pygame.Rect((0,0), (self.largura, self.altura))
        self.fonte = pygame.font.SysFont('arial', 32, True, False)
        self.list_dimenssoes_tela = [self.borda]
        return self

    def vars_tela_inicial(self):
        self.blit_xy_player1 = pygame.Rect(245,170, 170, 0)
        self.blit_xy_player2 = pygame.Rect(245,230, 230, 0)
        self.rect_botao_player1 = pygame.Rect(240,170,120,40)
        self.rect_botao_player2 = pygame.Rect(240,230,120,40)
        self.rect_botao_sublinhar_mod_player = pygame.Rect(245,210,0,5) 
        self.rect_botao_sublinhar_mod_player2 = pygame.Rect(245,270,0,5)
        self.blit_xy_clink = pygame.Rect(40,520, 0, 0)
        self.clink_rect = pygame.Rect(40,522,280,30)
        self.rect_botao_sublinhar_clink = pygame.Rect(40,558,0,3)
        self.list_tela_inicial = [self.rect_botao_player1,
                                    self.rect_botao_player2,
                                    self.blit_xy_player1,
                                    self.blit_xy_player2,
                                    self.rect_botao_sublinhar_mod_player,
                                    self.rect_botao_sublinhar_mod_player2,
                                    self.blit_xy_clink,
                                    self.clink_rect,
                                    self.rect_botao_sublinhar_clink]
        return self
    
    def vars_pre_start(self):
        self.rect_botao_voltar = pygame.Rect(40,300,85,30)
        self.rect_botao_sublinhar_voltar = pygame.Rect(40,340,0,3)
        self.mesgc_blit_xy = pygame.Rect(60,240, 0, 0)
        self.mesg_fj_blit_xy = pygame.Rect(215,225, 0, 0)
        self.blit_xy_voltar = pygame.Rect(40,300, 0, 0)
        self.blit_xy_mesg1_pontos = pygame.Rect(40,430, 0, 0)
        self.blit_xy_mesg_bp1 = pygame.Rect(40,530, 0, 0)   
        self.blit_xy_exibe_nivel = pygame.Rect(40,480, 0, 0)     
        self.blit_xy_mesg2_pontos = pygame.Rect(40,430, 0, 0)
        self.blit_xy_mesg_bp2 = pygame.Rect(40,530, 0, 0)
        self.blit_xy_iniciar1 = pygame.Rect(100,205, 0, 0)
        self.blit_xy_iniciar2 = pygame.Rect(55,270, 0, 0)
        self.list_pre_start = [self.rect_botao_voltar,
                                self.rect_botao_sublinhar_voltar,
                                self.mesgc_blit_xy,
                                self.mesg_fj_blit_xy,
                                self.blit_xy_voltar,
                                self.blit_xy_mesg1_pontos,
                                self.blit_xy_mesg_bp1,
                                self.blit_xy_exibe_nivel,
                                self.blit_xy_mesg2_pontos,
                                self.blit_xy_mesg_bp2,
                                self.blit_xy_iniciar1,
                                self.blit_xy_iniciar2]
        return self

    def vars_tela_config(self):
        self.rect_resolucao_texto1 = pygame.Rect(0,0,0,0) # 240,170,120,40
        self.rect_resolucao_texto2 = pygame.Rect(240,230,120,40)
        self.rect_resolucao_texto3 = pygame.Rect(240,290,120,40)
        self.img_xy = pygame.Rect(475,495, 0, 0)
        self.rect_botao_config = pygame.Rect(474.5,494.0,53.0,53.0)
        self.blit_xy_resolucao_texto1 = pygame.Rect(245,170, 0, 0)
        self.blit_xy_resolucao_texto2 = pygame.Rect(245,230, 0, 0)
        self.blit_xy_resolucao_texto3 = pygame.Rect(232,290, 0, 0)
        self.list_tela_config = [self.rect_resolucao_texto1,
                                    self.rect_resolucao_texto2,
                                    self.rect_resolucao_texto3,
                                    self.blit_xy_resolucao_texto1,
                                    self.blit_xy_resolucao_texto2,
                                    self.blit_xy_resolucao_texto3,
                                    self.img_xy, 
                                    self.rect_botao_config]
        return self

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
        self.tela.blit(texto_formatado, self.mesgc_blit_xy)
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

        self.rect_botao_sublinhar_mod_player.width = min(self.rect_botao_sublinhar_mod_player.width, 120)
        self.rect_botao_sublinhar_mod_player.width = max(self.rect_botao_sublinhar_mod_player.width, 0)
        self.rect_botao_sublinhar_mod_player2.width = min(self.rect_botao_sublinhar_mod_player2.width, 122)
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
            self.rect_botao_sublinhar_voltar.width += 86 
        else:
            self.cor_botao_voltar = (255,255,255)
            self.cor_botao_subl = (200,200,200)
            self.rect_botao_sublinhar_voltar.width -= 86

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
                        self.redimensionar.calculo_obter_proporcao((600,600))
                        self.config_button.copy_surface.fill((0,0,0))
                        return
                    elif rect2.collidepoint(pygame.mouse.get_pos()):
                        self.list_tela_config[0] = pygame.Rect(240,170,120,40)
                        self.redimensionar.calculo_obter_proporcao((800,720))
                        self.config_button.copy_surface.fill((0,0,0))
                        return
                    # elif rect3.collidepoint(pygame.mouse.get_pos()):
                    #     self.redimensionar.calculo_obter_proporcao(*pygame.display.list_modes()[0])  # Obtém a maior resolução suportada
                    #     return
                else:
                    self.tela.fill((0,0,0))
                    self.desenho_borda()
                    self.config_button.particao_desenho_botoes_resolucao()
                    pygame.display.update()

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

