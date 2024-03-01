

import json
import webbrowser

import pygame

from pygame._sdl2 import Renderer, Texture, Image, Window, messagebox

from src.core.player import Player
from src.core.player2 import Player2
from src.core.ball import Ball
from src.core.blocks import Blocks
from src.core.config_button import ConfigButton
from src.core.resize_Interface import ResizeInterface
from src.core.fonts import Fonts

from src.core.settings import COLOR_BUTTON_SUBLIME, ConfigVars 

class GameBase:
    def __init__(self):
        pygame.init()
        self.width = self.resolution_base[0]
        self.height = self.resolution_base[1]
        self.relative_height_ball = 180
        self.screen = pygame.display.set_mode(size=(self.width, self.height))
        self.border = pygame.Rect((0, 0), (self.width, self.height))
        self.dimension_list_screen = [self.border]

        self.resolution_base = (600, 600)
        self.resolution_base2 = (745, 690)
        self.modo_player1 = 'Player 1'
        self.modo_player2 = 'Player 2'
        self.back = f"Back"
        self.level = 1
        self.mens_level = f'Level: {self.level}'
        self.points2 = 0
        self.mens_points_2 = f'Points: {self.points2}'
        self.loading_lp2 = self.load_best_pontuation_player2()
        self.mens_bp2 = f'Best pontuation: {self.loading_lp2}'
        self.player_mode = None
        self.settings = ConfigVars(self)
        self.player = Player(self)
        self.player2 = Player2(self)
        self.ball = Ball(self)
        self.blocks = Blocks(self)
        self.fonts = Fonts()
        self.config_button = ConfigButton(self)
        self.resizeinterface = ResizeInterface(self)
        #self.mens_ite_init = f'Pressione a tecla "Enter" para iniciar'
            
    def load_best_pontuation_player2(self):
        try:
            with open('src/json/best_score2.json', 'r') as file:
                data = json.load(file)
                return data['best_score2']
        except (FileNotFoundError, KeyError):
            return 0

    def save_best_pontuation_player2(self):
        data = {'best_score2': self.loading_lp2}
        with open('src/json/best_score2.json', 'w') as file:
            json.dump(data, file)

    def update_best_pontuation_player2(self):
        if self.points2 > self.loading_lp2:
            self.loading_lp2 = self.points2
            self.save_best_pontuation_player2()
            self.mens_bp2 = f'Best pontuation: {self.loading_lp2}'

    def exibe_melhor_pontuacao2(self):
        mensagem = self.mens_bp2
        texo_formatado = self.fonts.font_candara.render(mensagem, False, (255, 255, 255))
        self.screen.blit(texo_formatado, self.settings.blit_xy_mesg_bp2)
    
    def exibir_pontuacao2(self):
        mensagem = self.mens_points_2
        texto_formatado = self.fonts.font_candara.render(mensagem, False, (255, 255, 255))
        self.screen.blit(texto_formatado, self.settings.blit_xy_mesg2_pontos)

    def atualiza_pontuacao2(self):
        self.points2 += 1
        self.mens_points_2 = f'Points: {self.points2}'

    def desenho_borda(self):
        pygame.draw.rect(self.screen, (115, 115, 115), self.border, 3)

    def animaçao_de_sublinhar_botao_tela_inicial(self):
        pygame.draw.rect(self.screen, COLOR_BUTTON_SUBLIME, self.settings.rect_botao_sublinhar_mod_player)
        pygame.draw.rect(self.screen, COLOR_BUTTON_SUBLIME, self.settings.rect_botao_sublinhar_mod_player2)
        pygame.draw.rect(self.screen, COLOR_BUTTON_SUBLIME, self.settings.rect_botao_sublinhar_clink)

        self.settings.rect_botao_sublinhar_mod_player.width = min(self.settings.rect_botao_sublinhar_mod_player.width, 120)
        self.settings.rect_botao_sublinhar_mod_player.width = max(self.settings.rect_botao_sublinhar_mod_player.width, 0)
        self.settings.rect_botao_sublinhar_mod_player2.width = min(self.settings.rect_botao_sublinhar_mod_player2.width, 122)
        self.settings.rect_botao_sublinhar_mod_player2.width = max(self.settings.rect_botao_sublinhar_mod_player2.width, 0)
        self.settings.rect_botao_sublinhar_clink.width = min(self.settings.rect_botao_sublinhar_clink.width, 3)
        self.settings.rect_botao_sublinhar_clink.width = max(self.settings.rect_botao_sublinhar_clink.width, 0)

    def botoes_tela_inicial_modos(self): # 1
        pos_mouse = pygame.mouse.get_pos()
        mod1 = self.modo_player1
        mod2 = self.modo_player2
        rect_modo1 = self.settings.rect_botao_player1
        rect_modo2 = self.settings.rect_botao_player2
        rect_c = self.settings.clink_rect
        
        self.cor_botao_modo1 = (170,170,170) if rect_modo1.collidepoint(pos_mouse) else (255,255,255)
        self.settings.rect_botao_sublinhar_mod_player.width += 3 if rect_modo1.collidepoint(pos_mouse) else -2

        self.cor_botao_modo2 = (170,170,170) if rect_modo2.collidepoint(pos_mouse) else (255,255,255)
        self.settings.rect_botao_sublinhar_mod_player2.width += 3 if rect_modo2.collidepoint(pos_mouse) else -2

        self.cor_clink = (170,170,170) if rect_c.collidepoint(pos_mouse) else (255,255,255)
        self.settings.rect_botao_sublinhar_clink.width += 280 if rect_c.collidepoint(pos_mouse) else -280

        if self.settings.rect_botao_player1.width > 0 and \
            self.settings.rect_botao_player2.width > 0 and \
            self.settings.clink_rect.width > 0:

            texto_formatado1 = self.fonts.font_arial.render(mod1, False, self.cor_botao_modo1)
            self.screen.blit(texto_formatado1, self.settings.blit_xy_player1)
            texto_formatado2 = self.fonts.font_arial.render(mod2, False, self.cor_botao_modo2)
            self.screen.blit(texto_formatado2, self.settings.blit_xy_player2)
            
            texto_clink = 'Criado por: Gabryel-lima'
            texto_formatado_c = self.fonts.font_impact.render(texto_clink, False, self.cor_clink)
            self.screen.blit(texto_formatado_c, self.settings.blit_xy_clink)

            self.config_button.button_config() # 2
            self.animaçao_de_sublinhar_botao_tela_inicial() # 3

    def executar_particao_proporcao_resolucao(self):
        self.resizeinterface.calculo_obter_proporcao(nova_resolucao=self.resolution_base)
        self.resizeinterface.calculo_obter_proporcao_blocos(nova_resolucao=self.resolution_base)
        self.resizeinterface.calculo_obter_proporcao_players(nova_resolucao=self.resolution_base)
        self.config_button.copy_surface.fill((0, 0, 0))

    def executar_particao_proporcao_resolucao2(self):
        self.settings.rect_resolucao_texto1 = pygame.Rect(240, 170, 120, 40)

        self.resizeinterface.calculo_obter_proporcao(nova_resolucao=self.resolution_base2)
        
        self.vars_screen_dimensions(resolution_base=self.resolution_base)

        self.resizeinterface.calculo_obter_proporcao_blocos(nova_resolucao=self.resolution_base2)
        self.resizeinterface.calculo_obter_proporcao_players(nova_resolucao=self.resolution_base2)
        
        self.config_button.copy_surface.fill((0, 0, 0))
    
    def executar_particao_desenho_botoes_resolucao(self, particao_config: None): # ou 5
        while True:
            for event in pygame.event.get():
                if event.type == pygame.constants.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    rect1, rect2, rect3 = self.config_button.partition_draw_buttons_resolutions()

                    if rect1.collidepoint(pygame.mouse.get_pos()):
                        self.executar_particao_proporcao_resolucao()
                        return
                    elif rect2.collidepoint(pygame.mouse.get_pos()):
                        self.executar_particao_proporcao_resolucao2()
                        return

            self.screen.fill((0, 0, 0))
            self.desenho_borda()
            particao_config()
            pygame.display.update()

    def desenho_botao_back(self) -> pygame.Rect:
        pos_mouse = pygame.mouse.get_pos()
        rect_botao = self.settings.rect_botao_voltar
        mensagem = self.back

        self.cor_botao_voltar = (150,150,150) if rect_botao.collidepoint(pos_mouse) else (255,255,255)
        self.settings.rect_botao_sublinhar_voltar.width += 68 if rect_botao.collidepoint(pos_mouse) else -6

        if self.settings.rect_botao_voltar.width > 0:  
            texto_formatado1 = self.fonts.font_arial.render(mensagem, False, self.cor_botao_voltar)
            self.screen.blit(texto_formatado1, self.settings.blit_xy_voltar)

            self.animaçao_de_sublinhar_botao_voltar()

        return rect_botao

    def animaçao_de_sublinhar_botao_voltar(self):
        pygame.draw.rect(self.screen, COLOR_BUTTON_SUBLIME, self.settings.rect_botao_sublinhar_voltar)

        self.settings.rect_botao_sublinhar_voltar.width = min(self.settings.rect_botao_sublinhar_voltar.width, 6)
        self.settings.rect_botao_sublinhar_voltar.width = max(self.settings.rect_botao_sublinhar_voltar.width, 0)

    def selecao_de_modos_estrutura(self): # 4 em decisão de onde o palyer vai interagir 
        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.settings.rect_botao_player1.collidepoint(pygame.mouse.get_pos()):
                    self.settings.rect_botao_player1 = pygame.Rect(0,0,0,0)
                    pygame.time.delay(300)
                    self.player_mode = "Player1"

                    self.executar_particao(particao=self.player.desenho_player)

                elif self.settings.rect_botao_player2.collidepoint(pygame.mouse.get_pos()):
                    self.settings.rect_botao_player2 = pygame.Rect(0,0,0,0)
                    pygame.time.delay(300)
                    self.player_mode = "Player2"

                    self.executar_particao(particao=self.player2.desenho_player)

                elif self.settings.clink_rect.collidepoint(pygame.mouse.get_pos()):
                    webbrowser.open("https://github.com/Gabryel-lima")
                    pygame.time.delay(300)
                
                elif self.settings.rect_botao_config.collidepoint(pygame.mouse.get_pos()):
                    self.config_button.draw_button_config(show=False)
                    pygame.time.delay(300)
                    
                    self.executar_particao_desenho_botoes_resolucao(particao_config=self.config_button.partition_draw_buttons_resolutions)

    def executar_particao(self, particao:None): # 5
        while True:
            for event in pygame.event.get():
                if event.type == pygame.constants.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.desenho_botao_back().collidepoint(pygame.mouse.get_pos()):
                        self.reset()
                        self.screen.fill((0, 0, 0))
                        pygame.time.delay(300)
                        return

                if event.type == pygame.constants.KEYDOWN and event.key == pygame.constants.K_RETURN:
                    self.settings.rect_botao_config = pygame.rect.Rect(0,0,0,0)
                    self.game_init = True
                    self.ball.iniciar_movimento()
                    if self.player_mode == "Player1":
                        self.player.reset()
                        self.player2.rect = pygame.rect.Rect(0,0,0,0)
                        self.screen.fill((0, 0, 0))
                        return
                    
                    elif self.player_mode == "Player2":
                        self.player.resetp_1()
                        self.player2.reset()
                        self.player2.rect = pygame.rect.Rect(self.player2.pos_x,
                                                 self.player2.pos_y,
                                                 self.player2.width_draw_x,
                                                 self.player2.height_draw_y)
                        self.screen.fill((0, 0, 0))
                        return

            self.screen.fill((0, 0, 0))
            self.desenho_botao_back()
            self.desenho_borda()
            self.ball.desenho_bola()
            self.blocks.desenhar_blocos()
            particao()
            pygame.display.update()

    def niveis_count(self):
        self.level += 1
        self.mens_level = f'Level: {self.level}'
                
    def manipula_nivel(self):
        while True:
            self.blocks.configurar_nivel()
            break

    def continuar_prox_nivel(self):
        self.game_init = True
        self.ball.iniciar_movimento()
        self.manipula_nivel()
        self.settings.rect_botao_player1 = pygame.Rect(0,0,0,0)
        self.settings.rect_botao_player2 = pygame.Rect(0,0,0,0)
        return

