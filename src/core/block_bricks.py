
# import sys
# import os

import json

import pygame
from pygame import *

from src.core.game_base import GameBase


# PROJECT_DIR = os.path.abspath('C:/Users/gabby/AndroidStudioProjects/Block_Bricks_Pygame')
# sys.path.append(PROJECT_DIR)


class Game(GameBase):
    def __init__(self):
        super().__init__()
        self.icon = pygame.image.load('assets/logo.ico')
        pygame.display.set_caption('Block-Bricks *1.7')
        pygame.display.set_icon(self.icon)
        self.clock_game = pygame.time.Clock()
        self.init_points = 0
        self.sound_over_level = pygame.mixer.Sound('sounds/som_fim_nivel.wav')
        self.sound_game_over = pygame.mixer.Sound('sounds/som_de_fim.wav')
        self.sound_collision = pygame.mixer.Sound('sounds/encosta_bloco.wav')
        self.mens_points = f'Pontos: {self.init_points}'
        self.loading_last_points = self.carregar_melhor_pontuacao()
        self.mens_bp = f'Melhor pontuação: {self.loading_last_points}'
        self.mens_game_over = f'Fim de jogo!'
        self.game_init = False

    def verify_height_ball(self):
        if self.ball.y + self.ball.raio >= self.height - self.relative_height_ball:
            text_format = self.fonts.font_arial.render(f'{self.mens_game_over}',
                                                        False,  (255, 255, 255))
            self.screen.blit(text_format, self.mesg_fj_blit_xy)

            self.particao_verificar_colisao()

    def verificar_colisao(self):
        if self.ball.bola_Rect.colliderect(self.player.rect):
            self.ball.inverter_direcao()

        elif self.ball.bola_Rect.colliderect(self.player2.rect):
            self.ball.inverter_direcao2()

        self.verify_height_ball()
            
        for blocks in self.blocks.lis_blocos:
            if self.ball.bola_Rect.colliderect(blocks):
                self.invert_direction_ball_block()
                self.som_da_bola_e_bloco()
                self.blocks.animacao_blocos(index=self.blocks.lis_blocos.index(blocks))
                self.blocks.lis_blocos.remove(blocks)
                if self.player_mode == "Player1":
                    self.atualiza_pontuacao()
                    self.atualiza_melhor_pontuacao()
                elif self.player_mode == "Player2":
                    self.atualiza_pontuacao2()
                    self.atualiza_melhor_pontuacao2()

    def particao_verificar_colisao(self):
        self.som_de_fim_de_jogo()
        pygame.display.flip()
        pygame.time.delay(3000)
        self.salvar_melhor_pontuacao()
        modo_selecionado = self.selecao_de_modos_estrutura()

        if modo_selecionado == self.executar_particao(particao=self.player.desenho_player):
            self.blocks.resetar_blocos()
            self.ball.reset()
            self.ball.iniciar_movimento()
            self.ball.atualizar()
            self.reset_pontos()
            self.reset_pontos2()
            self.reset_nivel()

        elif modo_selecionado == self.executar_particao(particao=self.player2.desenho_player):
            self.blocks.resetar_blocos()
            self.ball.reset()
            self.ball.iniciar_movimento()
            self.ball.atualizar()
            self.reset_pontos()
            self.reset_pontos2()
            self.reset_nivel()

    def som_da_bola_e_bloco(self):
        self.som = self.sound_collision
        self.som.set_volume(0.30)
        self.som.play()

    def som_de_fim_de_jogo(self):
        self.som = self.sound_game_over
        self.som.set_volume(0.30)
        self.som.play()

    def som_de_fim_de_nivel(self):
        self.som = self.sound_over_level
        self.som.set_volume(0.30)
        self.som.play()

    def carregar_melhor_pontuacao(self):
        try:
            with open('src/json/best_score.json', 'r') as file:
                data = json.load(file)
                return data['best_score']
        except (FileNotFoundError, KeyError):
            return 0

    def salvar_melhor_pontuacao(self):
        data = {'best_score': self.loading_last_points}
        with open('src/json/best_score.json', 'w') as file:
            json.dump(data, file)

    def atualiza_melhor_pontuacao(self):
        if self.init_points > self.loading_last_points:
            self.loading_last_points = self.init_points
            self.salvar_melhor_pontuacao()
            self.mens_bp = f'Melhor pontuação: {self.loading_last_points}'

    def reset_pontos2(self):
        if self.mensagem_fim_de_nivel == True:
            self.mesg2 = f'Pontos: {self.pontos2}'
        else:
            self.pontos2 = 0
            self.mesg2 = f'Pontos: {self.pontos2}'

    def reset_melhor_pontuacao(self): # Não está sendo utilizado.
        self.loading_last_points = 0
        self.salvar_melhor_pontuacao()
        pass

    def atualiza_pontuacao(self):
        self.init_points += 1
        self.mens_points = f'Pontos: {self.init_points}'

    def reset_pontos(self):
        if self.mensagem_fim_de_nivel == True:
            self.mens_points = f'Pontos: {self.init_points}'
        else:
            self.init_points = 0
            self.mens_points = f'Pontos: {self.init_points}'

    def reset_nivel(self):
        if self.mensagem_fim_de_nivel == True:
            self.mesg_nivel = f'Nivel: {self.nivel}'
        else:
            self.nivel = 1
            self.mesg_nivel = f'Nivel: {self.nivel}'

    def reset(self): # Esse metodo retorna o menu.
        if self.width == 600:
            self.game_init = False
            self.ball.reset()
            self.player.reset()
            self.player2.reset()
            self.rect_botao_player1 = self.list_tela_inicial[0]
            self.rect_botao_player2 = self.list_tela_inicial[1]
            self.rect_botao_config = self.list_tela_config[7]

        elif self.width > 600:
            self.game_init = False
            self.rect_botao_player1 = self.list_tela_inicial[0]
            self.rect_botao_player2 = self.list_tela_inicial[1]
            self.rect_botao_config = self.list_tela_config[7]

    def exibir_pontuacao(self):
        mensagem = self.mens_points
        texto_formatado = self.fonts.font_candara.render(mensagem, False, (255,255,255))
        self.screen.blit(texto_formatado, self.blit_xy_mesg1_pontos)

    def exibe_melhor_pontuacao(self):
        mensagem = self.mens_bp
        texo_formatado = self.fonts.font_candara.render(mensagem, False, (255,255,255))
        self.screen.blit(texo_formatado, self.blit_xy_mesg_bp1)

    def exibir_nivel(self):
        mensagem = self.mens_level
        texto_formatado = self.fonts.font_candara.render(mensagem, False, (255, 255, 255))
        self.screen.blit(texto_formatado, self.blit_xy_exibe_nivel)

    def mensagem_fim_de_nivel(self):
        if len(self.blocks.lis_blocos) == 0:
            texto_formatado = self.fonts.font_arial.render(f'fim do Nivel {self.level}', True, (255, 255, 255))
            self.screen.blit(texto_formatado, self.mesg_fj_blit_xy)
            self.niveis_count()
            self.som_de_fim_de_nivel()
            pygame.display.flip()
            pygame.time.delay(3000)
            self.blocks.resetar_blocos()
            self.ball.reset()
            self.continuar_prox_nivel()

    def colision_player_player2(self):
        if self.player.rect.colliderect(self.player2.rect) and pygame.key.get_pressed()[K_d]:
            self.player.pos_x -= 3.5
            if pygame.key.get_pressed()[K_LSHIFT]:
                self.player.pos_x -= 4.5
        
        if self.player2.rect.colliderect(self.player.rect) and pygame.key.get_pressed()[K_LEFT]:
            self.player2.pos_x += 3.5
            if pygame.key.get_pressed()[K_RSHIFT]:
                self.player2.pos_x += 4.5

    def invert_direction_ball_block(self):
        for block in self.blocks.lis_blocos:
            if self.ball.bola_Rect.colliderect(block):
                if self.ball.bola_Rect.centerx < block.right \
                        and block.left < self.ball.bola_Rect.centerx:
                    self.ball.VPos_y *= -1
                elif self.ball.bola_Rect.centery < block.bottom \
                        and block.top < self.ball.bola_Rect.centery:
                    self.ball.VPos_x *= -1
                else:
                    self.ball.VPos_y *= 1
                    self.ball.VPos_x *= 1
                    
    def layout(self):
        self.screen.fill((0, 0, 0))
        self.desenho_borda()
        self.botoes_tela_inicial_modos()
        self.selecao_de_modos_estrutura()
        
        if self.game_init:
            self.desenho_borda()
            self.ball.desenho_bola()
            self.blocks.desenhar_blocos()

            if self.player_mode == "Player1":
                self.player.desenho_player()

            elif self.player_mode == "Player2":
                self.player.desenho_player()
                self.player2.desenho_player()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            self.clock_game.tick(60)
            self.layout()

            if self.game_init:
                self.verificar_colisao()
                self.colision_player_player2()
                self.ball.atualizar()

                if self.player_mode == "Player1":
                    self.exibir_nivel()
                    self.exibe_melhor_pontuacao()
                    self.exibir_pontuacao()
                    self.player.player_collision()
                    self.player.input_player()

                elif self.player_mode == "Player2":
                    self.exibir_nivel()
                    self.exibe_melhor_pontuacao2()
                    self.exibir_pontuacao2()
                    self.player.player_collision()
                    self.player.input_player()
                    self.player2.player_collision()
                    self.player2.input_player2()

            self.mensagem_fim_de_nivel()
            pygame.display.update()

# def cprfi():

#     def mainProfile():
#         Game()

#     import cProfile
#     import pstats

#     profile = cProfile.Profile()
#     profile.enable()

#     mainProfile()

#     profile.disable()
#     stats = pstats.Stats(profile)
#     stats.strip_dirs()
#     stats.sort_stats('calls')
#     stats.print_stats()

# def main():
#     jogo = Jogo()
#     jogo.run()

# if __name__ == "__main__":
#     main()
