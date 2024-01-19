

import pygame
from pygame.locals import *


class Redimensionar_Interface:
    def __init__(self, jogo_base=object):
        self.jogo_base = jogo_base
        self.resolucao_orginal = (self.jogo_base.largura, self.jogo_base.altura)

    def for_dimenssoes_tela(self, nova_res=tuple, res_original=tuple): 
        nova = nova_res
        original = res_original
        for borda in self.jogo_base.list_dimensoes_tela:
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

    def for_pre_pos_start(self, nova_res=tuple, res_original=tuple):
        nova = nova_res
        original = res_original
        for start in self.jogo_base.list_pre_pos_start:
            start_copy = start.copy()
            x_ratio = nova[0] / original[0] 
            y_ratio = nova[1] / original[1]
            start.x = start_copy.x * x_ratio ##
            start.y = start_copy.y * y_ratio ##
        #print(self.jogo_base.list_pre_pos_start[9:])
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
    
    def calculo_obter_proporcao(self, nova_resolucao=tuple):
        nova_res = nova_resolucao
        res_original = self.resolucao_orginal
        
        if nova_res == res_original:
            self.jogo_base.vars_dimensoes_tela()
            self.jogo_base.vars_tela_inicial()
            self.jogo_base.vars_tela_config()
            self.jogo_base.vars_pre_pos_start()
        else:
            self.for_dimenssoes_tela(nova_res=nova_res, res_original=res_original)
            self.for_tela_inicial(nova_res=nova_res, res_original=res_original)
            self.for_pre_pos_start(nova_res=nova_res, res_original=res_original)
            self.for_tela_config(nova_res=nova_res, res_original=res_original)
            self.jogo_base.list_tela_config[1] = pygame.Rect(0,0,0,0)

    def calculo_obter_proporcao_blocos(self, nova_resolucao=tuple):
        nova_res = nova_resolucao 
        res_orginal = self.resolucao_orginal

        bloco_rect = self.jogo_base.blocos.bloco_Rect
        lis_blocos = self.jogo_base.blocos.lis_blocos

        if nova_res != res_orginal:
            for rect in lis_blocos:
                rect.width += bloco_rect.width 
                rect.height += bloco_rect.height 
            self.jogo_base.blocos.dimensionamento_espaco_blocos += 9
            self.jogo_base.blocos.dimensionamento_largura_bloco += 8 # Para alterar e centralizar os valores seria recomnedado mudar o espaço_blocos de multiplicação para adição ou subtração.
            self.jogo_base.blocos.dimensionamento_altura_bloco += 8 # Para alterar e centralizar os valores seria recomnedado mudar o espaço_blocos de multiplicação para adição ou subtração.

        else:
            for rect in lis_blocos:
                rect.width -= bloco_rect.width 
                rect.height -= bloco_rect.height
            self.jogo_base.blocos.dimensionamento_espaco_blocos -= 9
            self.jogo_base.blocos.dimensionamento_largura_bloco -= 8 # Para alterar e centralizar os valores seria recomnedado mudar o espaço_blocos de multiplicação para adição ou subtração.
            self.jogo_base.blocos.dimensionamento_altura_bloco -= 8 # Para alterar e centralizar os valores seria recomnedado mudar o espaço_blocos de multiplicação para adição ou subtração.
        
        self.jogo_base.blocos.lis_blocos.clear()
        self.jogo_base.blocos.criar_blocos()





