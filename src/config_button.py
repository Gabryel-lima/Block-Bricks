

import pygame
from pygame.locals import *


class ConfigButton:
    def __init__(self, jogo_base):
        self.jogo_base = jogo_base
        self.img_config_load = pygame.image.load('assets/gear_config.png')
        self.img_config = pygame.transform.scale(self.img_config_load, (50,50))
        self.img_xy = (475,495)
        self.resolucao_texto1 = f'600x600'
        self.resolucao_texto2 = f'800x800'
        self.resolucao_texto3 = f'Fullscreen'
        self.copy_surface = pygame.SurfaceType((50, 50), pygame.SRCALPHA)
        self.func_de_retorno = self.jogo_base.vars_tela_config() 

    def obter_valor_list(self, list_name=list, indice=int):
        return list_name[indice]

    def desenho_botao_config(self):
        self.copy_surface.blit(self.img_config, (0,0))
        self.func_de_retorno.tela.blit(self.copy_surface, self.img_xy)
        return self.func_de_retorno.rect_botao_config

    def botao_config(self):
        self.desenho_botao_config()
        pos_mouse = pygame.mouse.get_pos()

        if self.func_de_retorno.rect_botao_config.collidepoint(pos_mouse):
            scaled_copy = pygame.transform.scale_by(self.img_config, (1.1,1.1))
            self.func_de_retorno.tela.blit(scaled_copy, self.img_xy)
            return self.func_de_retorno.rect_botao_config

    def particao_desenho_botoes_resolucao(self):
        pos_mouse = pygame.mouse.get_pos()
        resolucao1 = self.resolucao_texto1
        resolucao2 = self.resolucao_texto2
        resolucao3 = self.resolucao_texto3
        rect1 = self.obter_valor_list(list_name=self.func_de_retorno.list_rect_resolucao_texto, indice=0)
        rect2 = self.obter_valor_list(list_name=self.func_de_retorno.list_rect_resolucao_texto, indice=1)
        rect3 = self.obter_valor_list(list_name=self.func_de_retorno.list_rect_resolucao_texto, indice=2)

        cor_rect_resolucao1 = (170,170,170) if rect1.collidepoint(pos_mouse) else (255,255,255)
        cor_rect_resolucao2 = (170,170,170) if rect2.collidepoint(pos_mouse) else (255,255,255)
        cor_rect_resolucao3 = (170,170,170) if rect3.collidepoint(pos_mouse) else (255,255,255)

        texto1 = self.func_de_retorno.fonte.render(resolucao1, False, cor_rect_resolucao1)
        self.func_de_retorno.tela.blit(texto1, (245,170))
        texto2 = self.func_de_retorno.fonte.render(resolucao2, False, cor_rect_resolucao2)
        self.func_de_retorno.tela.blit(texto2, (245,230))
        texto3 = self.func_de_retorno.fonte.render(resolucao3, False, cor_rect_resolucao3)
        self.func_de_retorno.tela.blit(texto3, (230,290))

        return rect1, rect2, rect3


