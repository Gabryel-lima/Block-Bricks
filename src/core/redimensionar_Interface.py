

import pygame
from pygame.locals import *


class Redimensionar_Interface:
    def __init__(self, jogo_base):
        self.jogo_base = jogo_base

    def for_dimenssoes_tela(self, nova_res=tuple, res_original=tuple): 
        nova = nova_res
        original = res_original
        for borda in self.jogo_base.list_dimenssoes_tela:
            borda_copy = borda.copy()
            x_ratio = nova[0] / original[0] 
            y_ratio = nova[1] / original[1]
            borda.x = borda_copy.x * x_ratio 
            borda.y = borda_copy.y * y_ratio
            borda.width = borda_copy.width * x_ratio
            borda.height = borda_copy.height * y_ratio
            self.jogo_base.tela = pygame.display.set_mode((borda.width, borda.height))
        return

    def for_tela_inicial(self, nova_res=tuple, res_original=tuple):
        nova = nova_res
        original = res_original
        for tela in self.jogo_base.list_tela_inicial:
            tela_copy = tela.copy()
            x_ratio = nova[0] / original[0] 
            y_ratio = nova[1] / original[1]
            tela.x = tela_copy.x * x_ratio
            tela.y = tela_copy.y * y_ratio
            tela.width = tela_copy.width
            tela.height = tela_copy.height
        return

    def for_pre_start(self, nova_res=tuple, res_original=tuple):
        nova = nova_res
        original = res_original
        for start in self.jogo_base.list_pre_start:
            start_copy = start.copy()
            x_ratio = nova[0] / original[0] 
            y_ratio = nova[1] / original[1]
            start.x = start_copy.x * x_ratio ##
            start.y = start_copy.y * y_ratio ##
            start.width = start_copy.width ##
            start.height = start_copy.height ##
        return

    def for_tela_config(self, nova_res=tuple, res_original=tuple):
        nova = nova_res
        original = res_original
        for config in self.jogo_base.list_tela_config:
            config_copy = config.copy()
            x_ratio = nova[0] / original[0] 
            y_ratio = nova[1] / original[1]
            config.x = config_copy.x * x_ratio ##
            config.y = config_copy.y * y_ratio ##
            config.width = config_copy.width * x_ratio
            config.height = config_copy.height * y_ratio
        return

    def redimensi_blocos(self, nova_res=tuple, res_original=tuple):
        nova = nova_res
        original = res_original

        bloco_rect = self.jogo_base.blocos.bloco_Rect
        lis_blocos = self.jogo_base.blocos.lis_blocos

        for rect in lis_blocos:
            rect_copy = rect.copy()
            bloco_rect.x = nova[0] / original[0] 
            bloco_rect.y = nova[1] / original[1]
            rect.x = rect_copy.x * bloco_rect.x ##
            rect.y = rect_copy.y * bloco_rect.y ##
            rect.width = rect_copy.width * bloco_rect.x
            rect.height = rect_copy.height * bloco_rect.y
        return
    
    def calculo_obter_proporcao(self, nova_resolucao=tuple):
        nova_res = nova_resolucao
        res_original = (self.jogo_base.largura, self.jogo_base.altura)
        
        if nova_res == res_original:
            self.jogo_base.vars_dimenssoes_tela()
            self.jogo_base.vars_tela_inicial()
            self.jogo_base.vars_tela_config()
            self.jogo_base.vars_pre_start()
        else:
            self.for_dimenssoes_tela(nova_res=nova_res, res_original=res_original)
            self.for_tela_inicial(nova_res=nova_res, res_original=res_original)
            self.for_pre_start(nova_res=nova_res, res_original=res_original)
            self.for_tela_config(nova_res=nova_res, res_original=res_original)
            self.redimensi_blocos(nova_res=nova_res, res_original=res_original)
            self.jogo_base.list_tela_config[1] = pygame.Rect(0,0,0,0)


