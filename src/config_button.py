
import os

import pygame
from pygame.locals import *


class ConfigButton:
    def __init__(self, jogo_base):
        self.jogo_base = jogo_base
        self.img_config_load = pygame.image.load('assets/gear_config.png')
        self.img_config = pygame.transform.scale(self.img_config_load, (50,50))
        self.img_xy = (475,495)
        self.rect_botao_config = pygame.Rect(474.5,494.0,53.0,53.0)
        self.resolucao_texto1 = f'600x600'
        self.resolucao_texto2 = f'800x800'
        self.resolucao_texto3 = f'Fullscreen'
        self.rect_resolucao_texto1 = Rect(240,170,120,40)
        self.rect_resolucao_texto2 = Rect(240,230,120,40)
        self.rect_resolucao_texto3 = Rect(240,290,120,40)
        self.copy_surface = pygame.SurfaceType
        self.list_rect_resolucao_texto = [self.rect_resolucao_texto1,
                                            self.rect_resolucao_texto2,
                                            self.rect_resolucao_texto3]

    def obter_valor_list(self, list_name=list, indice=int):
        return list_name[indice]

    def desenho_botao_config(self):
        self.copy_surface = pygame.Surface((50,50), pygame.SRCALPHA)
        self.copy_surface.blit(self.img_config, (0,0))
        self.jogo_base.tela.blit(self.copy_surface, self.img_xy)
        return self.rect_botao_config

    def botao_config(self):
        self.desenho_botao_config()
        pos_mouse = pygame.mouse.get_pos()

        if self.rect_botao_config.collidepoint(pos_mouse):
            scaled_copy = pygame.transform.scale_by(self.img_config, (1.1,1.1))
            self.jogo_base.tela.blit(scaled_copy, self.img_xy)
            return self.rect_botao_config

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

    def particao_desenho_botoes_resolucao(self):
        pos_mouse = pygame.mouse.get_pos()
        resolucao1 = self.resolucao_texto1
        resolucao2 = self.resolucao_texto2
        resolucao3 = self.resolucao_texto3
        rect1 = self.obter_valor_list(list_name=self.list_rect_resolucao_texto, indice=0)
        rect2 = self.obter_valor_list(list_name=self.list_rect_resolucao_texto, indice=1)
        rect3 = self.obter_valor_list(list_name=self.list_rect_resolucao_texto, indice=2)

        cor_rect_resolucao1 = (170,170,170) if rect1.collidepoint(pos_mouse) else (255,255,255)
        cor_rect_resolucao2 = (170,170,170) if rect2.collidepoint(pos_mouse) else (255,255,255)
        cor_rect_resolucao3 = (170,170,170) if rect3.collidepoint(pos_mouse) else (255,255,255)

        texto1 = self.jogo_base.fonte.render(resolucao1, False, cor_rect_resolucao1)
        self.jogo_base.tela.blit(texto1, (245,170))
        texto2 = self.jogo_base.fonte.render(resolucao2, False, cor_rect_resolucao2)
        self.jogo_base.tela.blit(texto2, (245,230))
        texto3 = self.jogo_base.fonte.render(resolucao3, False, cor_rect_resolucao3)
        self.jogo_base.tela.blit(texto3, (230,290))

        return rect1, rect2, rect3


