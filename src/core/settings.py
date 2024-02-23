import os
import pygame

PATH = os.path.abspath('.') + '/'

COLOR_BUTTON_SUBLIME = (250, 250, 250)


class ConfigVars:
    def __init__(self, game_base):
        self.game_base = game_base
        self._create_vars_tela_inicial()
        self._create_vars_pre_pos_start()
        self._create_vars_tela_config()

    @staticmethod
    def _create_rect(x: float, y: float, width: float, height: float):
        """Automatiza o processo de criação de novos rects nesta classe."""
        return pygame.Rect(x, y, width, height)

    @classmethod # @classmethod permite chamar diretamente os valores de objetos a serem usados ou modificados. 
    def _create_vars_tela_inicial(cls):
        """Por enquanto usada para criar e inicializar elementos na tela em determinada proporção \
            juntamente com um staticmethod _create_react para facilitar alguns processos de criação."""
        cls.blit_xy_player1 = cls._create_rect(245, 170, 170, 0)
        cls.blit_xy_player2 = cls._create_rect(245, 230, 230, 0)
        cls.rect_botao_player1 = cls._create_rect(240, 170, 120, 40)
        cls.rect_botao_player2 = cls._create_rect(240, 230, 120, 40)
        cls.rect_botao_sublinhar_mod_player = cls._create_rect(245, 210, 0, 5)
        cls.rect_botao_sublinhar_mod_player2 = cls._create_rect(245, 270, 0, 5)
        cls.blit_xy_clink = cls._create_rect(40, 520, 0, 0)
        cls.clink_rect = cls._create_rect(40, 522, 280, 30)
        cls.rect_botao_sublinhar_clink = cls._create_rect(40, 558, 0, 3)
        return {
            'rect_botao_player1': cls.rect_botao_player1,
            'rect_botao_player2': cls.rect_botao_player2,
            'blit_xy_player1': cls.blit_xy_player1,
            'blit_xy_player2': cls.blit_xy_player2,
            'rect_botao_sublinhar_mod_player': cls.rect_botao_sublinhar_mod_player,
            'rect_botao_sublinhar_mod_player2': cls.rect_botao_sublinhar_mod_player2,
            'blit_xy_clink': cls.blit_xy_clink,
            'clink_rect': cls.clink_rect,
            'rect_botao_sublinhar_clink': cls.rect_botao_sublinhar_clink
        }

    @classmethod
    def _create_vars_pre_pos_start(cls):
        """Por enquanto usada para criar e inicializar elementos na tela em determinada proporção \
            juntamente com um staticmethod _create_react para facilitar alguns processos de criação."""
        cls.rect_botao_voltar = cls._create_rect(40, 300, 85, 30)
        cls.rect_botao_sublinhar_voltar = cls._create_rect(40, 340, 0, 3)
        cls.mesg_fj_blit_xy = cls._create_rect(215, 225, 0, 0)
        cls.blit_xy_voltar = cls._create_rect(40, 300, 0, 0)
        cls.blit_xy_mesg1_pontos = cls._create_rect(40, 430, 0, 0)
        cls.blit_xy_mesg_bp1 = cls._create_rect(40, 530, 0, 0)
        cls.blit_xy_exibe_nivel = cls._create_rect(40, 480, 0, 0)
        cls.blit_xy_mesg2_pontos = cls._create_rect(40, 430, 0, 0)
        cls.blit_xy_mesg_bp2 = cls._create_rect(40, 530, 0, 0)
        return {
            'rect_botao_voltar': cls.rect_botao_voltar,
            'rect_botao_sublinhar_voltar': cls.rect_botao_sublinhar_voltar,
            'mesg_fj_blit_xy': cls.mesg_fj_blit_xy,
            'blit_xy_voltar': cls.blit_xy_voltar,
            'blit_xy_mesg1_pontos': cls.blit_xy_mesg1_pontos,
            'blit_xy_mesg_bp1': cls.blit_xy_mesg_bp1,
            'blit_xy_exibe_nivel': cls.blit_xy_exibe_nivel,
            'blit_xy_mesg2_pontos': cls.blit_xy_mesg2_pontos,
            'blit_xy_mesg_bp2': cls.blit_xy_mesg_bp2
        }

    @classmethod
    def _create_vars_tela_config(cls):
        """Por enquanto usada para criar e inicializar elementos na tela em determinada proporção \
            juntamente com um staticmethod _create_react para facilitar alguns processos de criação."""
        cls.rect_resolucao_texto1 = cls._create_rect(0, 0, 0, 0)  # 240,170,120,40
        cls.rect_resolucao_texto2 = cls._create_rect(240, 230, 120, 40)
        cls.rect_resolucao_texto3 = cls._create_rect(240, 290, 120, 40)
        cls.img_xy = cls._create_rect(475, 495, 0, 0)
        cls.rect_botao_config = cls._create_rect(474.5, 494.0, 53.0, 53.0)
        cls.blit_xy_resolucao_texto1 = cls._create_rect(245, 170, 0, 0)
        cls.blit_xy_resolucao_texto2 = cls._create_rect(245, 230, 0, 0)
        cls.blit_xy_resolucao_texto3 = cls._create_rect(232, 290, 0, 0)
        return {
            'rect_resolucao_texto1': cls.rect_resolucao_texto1,
            'rect_resolucao_texto2': cls.rect_resolucao_texto2,
            'rect_resolucao_texto3': cls.rect_resolucao_texto3,
            'blit_xy_resolucao_texto1': cls.blit_xy_resolucao_texto1,
            'blit_xy_resolucao_texto2': cls.blit_xy_resolucao_texto2,
            'blit_xy_resolucao_texto3': cls.blit_xy_resolucao_texto3,
            'img_xy': cls.img_xy,
            'rect_botao_config': cls.rect_botao_config
        }
    
    