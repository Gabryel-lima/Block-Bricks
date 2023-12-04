

import pygame
from pygame.locals import *



class ConfigButton:
    def __init__(self, tela):
        self.tela = tela
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

    def aplicar_resolucao(self, r1=Rect, r2=Rect, r3=Rect):
        pass

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
        rect1, rect2, rect3 = self.particao_desenho_botoes_resolucao()
        if rect1.collidepoint(pygame.mouse.get_pos()):
            self.aplicar_resolucao(r1=rect1)
        elif rect2.collidepoint(pygame.mouse.get_pos()):
            self.aplicar_resolucao(r2=rect2)
        elif rect3.collidepoint(pygame.mouse.get_pos()):
            self.aplicar_resolucao(r3=rect3)
