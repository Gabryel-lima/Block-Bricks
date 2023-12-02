

import pygame
from pygame.locals import *



class ConfigButton:
    def __init__(self, jogo_base, rect_botao_player):
        self.jogo_base = jogo_base
        self.rect_botao_player = rect_botao_player
        self.img_config = pygame.image.load('assets/gear_config.png')
        self.img_config = pygame.transform.scale(self.img_config, (50,50))
        self.img_xy = (475,495)
        self.rect_botao_config = pygame.Rect(474.5,494.0,53.0,53.0)
        self.copy_surface = pygame.SurfaceType
        #self.cor_botao_config = (255,255,255)

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

    def opcao_resolucao(self):
        pass
        

