

import pygame
from pygame.locals import *


class ConfigButton:
    def __init__(self, jogo_base):
        self.jogo_base = jogo_base
        self.img_config_load = pygame.image.load('assets/gear_config.png')
        self.img_config = pygame.transform.scale(self.img_config_load, (50,50))
        self.resolucao_texto1 = f'600x600'
        self.resolucao_texto2 = f'750x720'
        self.resolucao_texto3 = f'Fullscreen'
        self.copy_surface = pygame.SurfaceType((50, 50), pygame.SRCALPHA)
        self.func_vars_tela = self.jogo_base.vars_tela_config() 
        self.func_vars_config = self.jogo_base.vars_tela_config() # Duas instancias para legibilidade.
        
    def obter_valor_list(self, list_name=list, indice=int):
        return list_name[indice]

    def desenho_botao_config(self):
        self.copy_surface.blit(self.img_config, (0,0))
        self.func_vars_tela.tela.blit(self.copy_surface, self.func_vars_tela.img_xy)
        return self.func_vars_tela.rect_botao_config

    def botao_config(self):
        self.desenho_botao_config()
        pos_mouse = pygame.mouse.get_pos()

        if self.func_vars_tela.rect_botao_config.collidepoint(pos_mouse):
            scaled_copy = pygame.transform.scale_by(self.img_config, (1.1,1.1))
            self.func_vars_tela.tela.blit(scaled_copy, self.func_vars_tela.img_xy)
            return self.func_vars_tela.rect_botao_config

    def particao_desenho_botoes_resolucao(self):
        pos_mouse = pygame.mouse.get_pos()
        resolucao1 = self.resolucao_texto1
        resolucao2 = self.resolucao_texto2
        resolucao3 = self.resolucao_texto3
        rect1 = self.obter_valor_list(list_name=self.func_vars_tela.list_tela_config, indice=0)
        rect2 = self.obter_valor_list(list_name=self.func_vars_tela.list_tela_config, indice=1)
        rect3 = self.obter_valor_list(list_name=self.func_vars_tela.list_tela_config, indice=2)

        cor_rect_resolucao1 = (170,170,170) if rect1.collidepoint(pos_mouse) else (255,255,255)
        cor_rect_resolucao2 = (170,170,170) if rect2.collidepoint(pos_mouse) else (255,255,255)
        cor_rect_resolucao3 = (170,170,170) if rect3.collidepoint(pos_mouse) else (255,255,255)

        texto1 = self.func_vars_tela.fonte.render(resolucao1, False, cor_rect_resolucao1)
        self.func_vars_tela.tela.blit(texto1, self.func_vars_config.blit_xy_resolucao_texto1)
        texto2 = self.func_vars_tela.fonte.render(resolucao2, False, cor_rect_resolucao2)
        self.func_vars_tela.tela.blit(texto2, self.func_vars_config.blit_xy_resolucao_texto2)
        texto3 = self.func_vars_tela.fonte.render(resolucao3, False, cor_rect_resolucao3)
        self.func_vars_tela.tela.blit(texto3, self.func_vars_config.blit_xy_resolucao_texto3)

        return rect1, rect2, rect3


