import os
import pygame

PATH = os.path.abspath('.') + '/'

COLOR_BUTTON_SUBLIME = (250, 250, 250)


class ConfigVars:
    def __init__(self, game_base):
        self.game_base = game_base

    @staticmethod
    def _create_rect(x: float, y: float, width: float, height: float):
        """Automatiza o processo de criação de novos rects nesta classe."""
        return pygame.Rect(x, y, width, height)

    @classmethod
    def get_vars_tela_inicial(cls):
        return cls._create_vars_tela_inicial()

    @classmethod
    def get_vars_pre_pos_start(cls):
        return cls._create_vars_pre_pos_start()

    @classmethod
    def get_vars_tela_config(cls):
        return cls._create_vars_tela_config()

    @staticmethod
    def _create_vars_tela_inicial():
        blit_xy_player1 = ConfigVars._create_rect(245, 170, 170, 0)
        blit_xy_player2 = ConfigVars._create_rect(245, 230, 230, 0)
        rect_botao_player1 = ConfigVars._create_rect(240, 170, 120, 40)
        rect_botao_player2 = ConfigVars._create_rect(240, 230, 120, 40)
        rect_botao_sublinhar_mod_player = ConfigVars._create_rect(245, 210, 0, 5)
        rect_botao_sublinhar_mod_player2 = ConfigVars._create_rect(245, 270, 0, 5)
        blit_xy_clink = ConfigVars._create_rect(40, 520, 0, 0)
        clink_rect = ConfigVars._create_rect(40, 522, 280, 30)
        rect_botao_sublinhar_clink = ConfigVars._create_rect(40, 558, 0, 3)
        return {
            'rect_botao_player1': rect_botao_player1,
            'rect_botao_player2': rect_botao_player2,
            'blit_xy_player1': blit_xy_player1,
            'blit_xy_player2': blit_xy_player2,
            'rect_botao_sublinhar_mod_player': rect_botao_sublinhar_mod_player,
            'rect_botao_sublinhar_mod_player2': rect_botao_sublinhar_mod_player2,
            'blit_xy_clink': blit_xy_clink,
            'clink_rect': clink_rect,
            'rect_botao_sublinhar_clink': rect_botao_sublinhar_clink
        }

    @staticmethod
    def _create_vars_pre_pos_start():
        rect_botao_voltar = ConfigVars._create_rect(40, 300, 85, 30)
        rect_botao_sublinhar_voltar = ConfigVars._create_rect(40, 340, 0, 3)
        mesg_fj_blit_xy = ConfigVars._create_rect(215, 225, 0, 0)
        blit_xy_voltar = ConfigVars._create_rect(40, 300, 0, 0)
        blit_xy_mesg1_pontos = ConfigVars._create_rect(40, 430, 0, 0)
        blit_xy_mesg_bp1 = ConfigVars._create_rect(40, 530, 0, 0)
        blit_xy_exibe_nivel = ConfigVars._create_rect(40, 480, 0, 0)
        blit_xy_mesg2_pontos = ConfigVars._create_rect(40, 430, 0, 0)
        blit_xy_mesg_bp2 = ConfigVars._create_rect(40, 530, 0, 0)
        return {
            'rect_botao_voltar': rect_botao_voltar,
            'rect_botao_sublinhar_voltar': rect_botao_sublinhar_voltar,
            'mesg_fj_blit_xy': mesg_fj_blit_xy,
            'blit_xy_voltar': blit_xy_voltar,
            'blit_xy_mesg1_pontos': blit_xy_mesg1_pontos,
            'blit_xy_mesg_bp1': blit_xy_mesg_bp1,
            'blit_xy_exibe_nivel': blit_xy_exibe_nivel,
            'blit_xy_mesg2_pontos': blit_xy_mesg2_pontos,
            'blit_xy_mesg_bp2': blit_xy_mesg_bp2
        }

    @staticmethod
    def _create_vars_tela_config():
        rect_resolucao_texto1 = ConfigVars._create_rect(0, 0, 0, 0)  # 240,170,120,40
        rect_resolucao_texto2 = ConfigVars._create_rect(240, 230, 120, 40)
        rect_resolucao_texto3 = ConfigVars._create_rect(240, 290, 120, 40)
        img_xy = ConfigVars._create_rect(475, 495, 0, 0)
        rect_botao_config = ConfigVars._create_rect(474.5, 494.0, 53.0, 53.0)
        blit_xy_resolucao_texto1 = ConfigVars._create_rect(245, 170, 0, 0)
        blit_xy_resolucao_texto2 = ConfigVars._create_rect(245, 230, 0, 0)
        blit_xy_resolucao_texto3 = ConfigVars._create_rect(232, 290, 0, 0)
        return {
            'rect_resolucao_texto1': rect_resolucao_texto1,
            'rect_resolucao_texto2': rect_resolucao_texto2,
            'rect_resolucao_texto3': rect_resolucao_texto3,
            'blit_xy_resolucao_texto1': blit_xy_resolucao_texto1,
            'blit_xy_resolucao_texto2': blit_xy_resolucao_texto2,
            'blit_xy_resolucao_texto3': blit_xy_resolucao_texto3,
            'img_xy': img_xy,
            'rect_botao_config': rect_botao_config
        }
    
    