import os
import pygame

PATH = os.path.abspath('.') + '/'

COLOR_BUTTON_SUBLIME = (250, 250, 250)

from icecream import ic

class ConfigVars:
    def __init__(self, game_base):
        self.game_base = game_base
        self.list_tela_inicial = self._create_vars_tela_inicial()
        self.list_pre_pos = self._create_vars_pre_pos_start()
        self.list_tela_config = self._create_vars_tela_config()

    @staticmethod
    def _create_rect(x: float, y: float, width: float, height: float) -> pygame.Rect:
        """Automatiza o processo de criação de novos rects nesta classe."""
        return pygame.Rect(x, y, width, height)

    def _create_vars_tela_inicial(self):
        """Por enquanto usada para criar e inicializar elementos na tela em determinada proporção \
            juntamente com um staticmethod _create_react para facilitar alguns processos de criação."""
        self.blit_xy_player1 = self._create_rect(245, 170, 170, 0)
        self.blit_xy_player2 = self._create_rect(245, 230, 230, 0)
        self.rect_botao_player1 = self._create_rect(240, 170, 120, 40)
        self.rect_botao_player2 = self._create_rect(240, 230, 120, 40)
        self.rect_botao_sublinhar_mod_player = self._create_rect(245, 210, 0, 5)
        self.rect_botao_sublinhar_mod_player2 = self._create_rect(245, 270, 0, 5)
        self.blit_xy_clink = self._create_rect(40, 520, 0, 0)
        self.clink_rect = self._create_rect(40, 522, 280, 30)
        self.rect_botao_sublinhar_clink = self._create_rect(40, 558, 0, 3)
        return []

    def _create_vars_pre_pos_start(self):
        """Por enquanto usada para criar e inicializar elementos na tela em determinada proporção \
            juntamente com um staticmethod _create_react para facilitar alguns processos de criação."""
        self.rect_botao_voltar = self._create_rect(40, 300, 85, 30)
        self.rect_botao_sublinhar_voltar = self._create_rect(40, 340, 0, 3)
        self.mesg_fj_blit_xy = self._create_rect(215, 225, 0, 0)
        self.blit_xy_voltar = self._create_rect(40, 300, 0, 0)
        self.blit_xy_mesg1_pontos = self._create_rect(40, 430, 0, 0)
        self.blit_xy_mesg_bp1 = self._create_rect(40, 530, 0, 0)
        self.blit_xy_exibe_nivel = self._create_rect(40, 480, 0, 0)
        self.blit_xy_mesg2_pontos = self._create_rect(40, 430, 0, 0)
        self.blit_xy_mesg_bp2 = self._create_rect(40, 530, 0, 0)
        return []

    def _create_vars_tela_config(self):
        """Por enquanto usada para criar e inicializar elementos na tela em determinada proporção \
            juntamente com um staticmethod _create_react para facilitar alguns processos de criação."""
        self.rect_resolucao_texto1 = self._create_rect(0, 0, 0, 0)  # 240,170,120,40
        self.rect_resolucao_texto2 = self._create_rect(240, 230, 120, 40)
        self.rect_resolucao_texto3 = self._create_rect(240, 290, 120, 40)
        self.img_xy = self._create_rect(475, 495, 0, 0)
        self.rect_botao_config = self._create_rect(474.5, 494.0, 53.0, 53.0)
        self.blit_xy_resolucao_texto1 = self._create_rect(245, 170, 0, 0)
        self.blit_xy_resolucao_texto2 = self._create_rect(245, 230, 0, 0)
        self.blit_xy_resolucao_texto3 = self._create_rect(232, 290, 0, 0)
        return []

    
    