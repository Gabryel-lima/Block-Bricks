
import os

import pygame
from pygame.locals import *



class ConfigButton:
    def __init__(self, jogo_base):
        self.jogo_base = jogo_base
        self.resolucao_atual = (600,600)
        self.largura = 600
        self.altura = 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.borda = pygame.Rect(0, 0, self.largura, self.altura)
        self.fonte = pygame.font.SysFont('arial', 30, True, False)
        self.img_config_load = pygame.image.load('assets/gear_config.png')
        self.img_config = pygame.transform.scale(self.img_config_load, (50,50))
        self.img_xy = (475,495)
        self.rect_botao_config = pygame.Rect(474.5,494.0,53.0,53.0)
        self.resolucao_texto1 = f'600x600'
        self.resolucao_texto2 = f'800x800'
        self.resolucao_texto3 = f'Fullscreen'
        self.rect_resolucao_texto1 = pygame.Rect(240,170,120,40)
        self.rect_resolucao_texto2 = pygame.Rect(240,230,120,40)
        self.rect_resolucao_texto3 = pygame.Rect(240,290,120,40)
        self.copy_surface = pygame.SurfaceType

    def desenho_botao_config(self):
        self.copy_surface = pygame.Surface((50,50), pygame.SRCALPHA)
        self.copy_surface.blit(self.img_config, (0,0))
        self.tela.blit(self.copy_surface, self.img_xy)
        return self.rect_botao_config

    def botao_config(self):
        self.desenho_botao_config()
        pos_mouse = pygame.mouse.get_pos()

        if self.rect_botao_config.collidepoint(pos_mouse):
            scaled_copy = pygame.transform.scale_by(self.img_config, (1.1,1.1))
            self.tela.blit(scaled_copy, self.img_xy)

    def alterna_tela_inicial(self, limpar=bool):
        if limpar:
            self.rect_botao_player1 = Rect(0,0,0,0)
            self.rect_botao_player2 = Rect(0,0,0,0)
            self.clink_rect = Rect(0,0,0,0)
            self.rect_botao_config = Rect(0,0,0,0)
            self.img_xy = (0,0)
            self.img_config_load = pygame.Surface(self.img_config.get_size())
        else:
            self.rect_botao_player1 = pygame.Rect(240,170,120,40)
            self.rect_botao_player2 = pygame.Rect(240,230,120,40) 
            self.clink_rect = pygame.Rect(40,522,280,30)
            self.rect_botao_config = pygame.Rect(474.5,494.0,53.0,53.0)
            self.img_xy = (475,495)
            self.img_config_load = pygame.image.load('assets/gear_config.png')

    def aplicar_resolucao(self, largura, altura):
        if (largura, altura) != self.resolucao_atual:
            self.tela = pygame.display.set_mode((largura, altura))
            self.resolucao_atual = (largura, altura)
            if (largura, altura) == (600,600):
                self.tela = pygame.display.set_mode((largura, altura))
                self.resolucao_atual = (largura, altura)
                self.borda = pygame.Rect((0,0), (600,600))
                self.blit_xy_mod1 = (245,170)
                self.blit_xy_mod2 = (245,230)
                self.rect_botao_player1 = pygame.Rect(240,170,120,40)
                self.rect_botao_player2 = pygame.Rect(240,230,120,40)
                self.rect_botao_voltar = pygame.Rect(40,300,85,30)
                self.rect_botao_sublinhar_mod_player = pygame.Rect(245,210,0,5) #(240,210,0,5) #240,170,120,40
                self.rect_botao_sublinhar_mod_player2 = pygame.Rect(245,270,0,5)
                self.rect_botao_sublinhar_clink = pygame.Rect(40,558,0,3)
                self.rect_botao_sublinhar_voltar = pygame.Rect(40,340,0,3) 
                self.clink_rect = pygame.Rect(40,522,280,30)
                self.rect_botao_config = pygame.Rect(50,50,50,50)

            elif (largura, altura) == (800,800):
                self.tela = pygame.display.set_mode((largura, altura))
                self.resolucao_atual = (largura, altura)
                self.borda = pygame.Rect((0,0), (800,800))
                

            else:
                #self.aplicar_resolucao(*pygame.display.list_modes()[0])
                self.borda = pygame.Rect((0,0), (largura, altura))
                

    def particao_desenho_botoes_resolucao(self):
        pos_mouse = pygame.mouse.get_pos()
        resolucao1 = self.resolucao_texto1
        resolucao2 = self.resolucao_texto2
        resolucao3 = self.resolucao_texto3
        rect1 = self.rect_resolucao_texto1
        rect2 = self.rect_resolucao_texto2
        rect3 = self.rect_resolucao_texto3

        cor_rect_resolucao1 = (170,170,170) if rect1.collidepoint(pos_mouse) else (255,255,255)
        cor_rect_resolucao2 = (170,170,170) if rect2.collidepoint(pos_mouse) else (255,255,255)
        cor_rect_resolucao3 = (170,170,170) if rect3.collidepoint(pos_mouse) else (255,255,255)

        texto1 = self.fonte.render(resolucao1, False, cor_rect_resolucao1)
        self.tela.blit(texto1, (245,170))
        texto2 = self.fonte.render(resolucao2, False, cor_rect_resolucao2)
        self.tela.blit(texto2, (245,230))
        texto3 = self.fonte.render(resolucao3, False, cor_rect_resolucao3)
        self.tela.blit(texto3, (230,290))

        return rect1, rect2, rect3

    def executar_particao_desenho_botoes_resolucao(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    os._exit(0)

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    rect1, rect2, rect3 = self.particao_desenho_botoes_resolucao()

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
                    self.jogo_base.desenho_botao_back()
                    self.jogo_base.desenho_borda()
                    self.particao_desenho_botoes_resolucao()
                    pygame.display.update()
