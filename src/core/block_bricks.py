
import sys
sys.path.append('C:/Users/gabry/OneDrive/Área de Trabalho/Block-Bricks Pygame/src')

import json
import os

import pygame
from pygame.locals import *

from jogo_base import JogoBase


class Jogo(JogoBase):
    def __init__(self):
        super().__init__()
        self.icon = pygame.image.load('assets/logo.ico')
        pygame.display.set_caption('Block-Bricks *1.7')
        pygame.display.set_icon(self.icon)
        self.relogio = pygame.time.Clock()
        self.pontos = 0
        self.som_fim_nivel = pygame.mixer.Sound('sounds/som_fim_nivel.wav')
        self.fim_jogo = pygame.mixer.Sound('sounds/som_de_fim.wav')
        self.som_colisao = pygame.mixer.Sound('sounds/encosta_bloco.wav')
        self.mesgc = f'"A"<Esquerda, "D">Direita, "LShift"<Aceleração>'
        self.mesgc2 = f'"<-"<Esquerda, "->">Direita, "RShift"<Aceleração>'
        self.mesg = f'Pontos: {self.pontos}'
        self.lp = self.carregar_melhor_pontuacao()
        self.mesg_bp = f'Melhor pontuação: {self.lp}'
        self.mesg_fj = 'Fim de jogo!'
        self.fontei = pygame.font.SysFont('Candara', 30, True, False)
        self.jogo_iniciado = False

    def verifica_altura_bola(self):
        if self.bola.y + self.bola.raio >= self.altura - self.altura_relativa_bola:
            texto_formatado = self.fonte.render(f'{self.mesg_fj}', False, (255,255,255))  
            self.tela.blit(texto_formatado, self.mesg_fj_blit_xy)

            self.particao_verificar_colisao()

    def verificar_colisao(self):
        if self.bola.bola_Rect.colliderect(self.player.rect):
            self.bola.inverter_direcao()

        elif self.bola.bola_Rect.colliderect(self.player2.rect):     
            self.bola.inverter_direcao2()

        #elif self.bola.rect.colliderect(self.bot.rectb):
            #self.bola.inverter_direcao()

        self.verifica_altura_bola()
            
        for bloco in self.blocos.lis_blocos:
            if self.bola.bola_Rect.colliderect(bloco):
                self.inverter_direcao_bola_bloco()
                self.som_da_bola_e_bloco()
                self.blocos.animacao_blocos(index=self.blocos.lis_blocos.index(bloco))
                self.blocos.lis_blocos.remove(bloco)
                if self.modo_jogador == "Player1":
                    self.atualiza_pontuacao()
                    self.atualiza_melhor_pontuacao()
                elif self.modo_jogador == "Player2":
                    self.atualiza_pontuacao2()
                    self.atualiza_melhor_pontuacao2()
                break

    def particao_verificar_colisao(self):
        self.som_de_fim_de_jogo()
        pygame.display.flip()
        pygame.time.delay(3000)
        self.salvar_melhor_pontuacao()
        modo_selecionado = self.selecao_de_modos_estrutura()

        if modo_selecionado == self.executar_particao(particao=self.selecao_de_modos_estrutura_particao):
            self.blocos.resetar_blocos()
            self.bola.reset()
            self.bola.iniciar_movimento()
            self.reset_pontos()
            self.reset_pontos2()
            self.reset_nivel()

        elif modo_selecionado == self.executar_particao(particao=self.selecao_de_modos_estrutura_particao2):
            self.blocos.resetar_blocos()
            self.bola.reset()
            self.bola.iniciar_movimento()
            self.selecao_de_modos_estrutura()
            self.reset_pontos()
            self.reset_pontos2()
            self.reset_nivel()

    def som_da_bola_e_bloco(self):
        self.som = self.som_colisao
        self.som.set_volume(0.30)
        self.som.play()

    def som_de_fim_de_jogo(self):
        self.som = self.fim_jogo
        self.som.set_volume(0.30)
        self.som.play()

    def som_de_fim_de_nivel(self):
        self.som = self.som_fim_nivel
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
        data = {'best_score': self.lp}
        with open('src/json/best_score.json', 'w') as file:
            json.dump(data, file)

    def atualiza_melhor_pontuacao(self):
        if self.pontos > self.lp:
            self.lp = self.pontos
            self.salvar_melhor_pontuacao()
            self.mesg_bp = f'Melhor pontuação: {self.lp}'

    def reset_pontos2(self):
        if self.mensagem_fim_de_nivel == True:
            self.mesg2 = f'Pontos: {self.pontos2}'
        else:
            self.pontos2 = 0
            self.mesg2 = f'Pontos: {self.pontos2}'

    def reset_melhor_pontuacao(self): # Não está sendo utilizado.
        self.lp = 0
        self.salvar_melhor_pontuacao()
        pass

    def atualiza_pontuacao(self):
        self.pontos += 1
        self.mesg = f'Pontos: {self.pontos}'

    def reset_pontos(self):
        if self.mensagem_fim_de_nivel == True:
            self.mesg = f'Pontos: {self.pontos}'
        else:
            self.pontos = 0
            self.mesg = f'Pontos: {self.pontos}'

    def reset_nivel(self):
        if self.mensagem_fim_de_nivel == True:
            self.mesg_nivel = f'Nivel: {self.nivel}'
        else:
            self.nivel = 1
            self.mesg_nivel = f'Nivel: {self.nivel}'

    def reset(self): # Esse metodo retorna o menu.
        if self.largura == 600:
            self.jogo_iniciado = False
            self.bola.reset()
            self.player.reset()
            self.player2.reset()
            self.rect_botao_player1 = self.list_tela_inicial[0]
            self.rect_botao_player2 = self.list_tela_inicial[1]

        elif self.largura > 600:
            self.jogo_iniciado = False
            self.rect_botao_player1 = self.list_tela_inicial[self]
            self.rect_botao_player2 = self.list_tela_inicial[self]

    def exibir_pontuacao(self):
        mensagem = self.mesg
        texto_formatado = self.fontei.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado,  self.blit_xy_mesg1_pontos)

    def exibe_melhor_pontuacao(self):
        mensagem = self.mesg_bp
        texo_formatado = self.fontei.render(mensagem, False, (255,255,255))
        self.tela.blit(texo_formatado, self.blit_xy_mesg_bp1)

    def exibir_nivel(self):
        mensagem = self.mesg_nivel
        texto_formatado = self.fontei.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, self.blit_xy_exibe_nivel)

    def mensagem_fim_de_nivel(self):
        if len(self.blocos.lis_blocos) == 0:
            texto_formatado = self.fonte.render(f'Fim do Nivel {self.nivel}', False, (255,255,255))  
            self.tela.blit(texto_formatado, self.blit_xy_nivel)
            self.niveis_count()
            self.som_de_fim_de_nivel()
            pygame.display.flip()
            pygame.time.delay(3000)
            self.blocos.resetar_blocos()
            self.bola.reset()
            self.continuar_prox_nivel()

    def colisao_player_player2(self):
        if self.player.rect.colliderect(self.player2.rect) and pygame.key.get_pressed()[K_d]:
            self.player.x -= 3.5
            if pygame.key.get_pressed()[K_LSHIFT]:
                self.player.x -= 4.5
        
        if self.player2.rect.colliderect(self.player.rect) and pygame.key.get_pressed()[K_LEFT]:
            self.player2.x += 3.5 
            if pygame.key.get_pressed()[K_RSHIFT]:
                self.player2.x += 4.5

    def inverter_direcao_bola_bloco(self):
        for bloco in self.blocos.lis_blocos:
            if self.bola.bola_Rect.colliderect(bloco):
                if self.bola.bola_Rect.centerx < bloco.right and bloco.left < self.bola.bola_Rect.centerx:
                    self.bola.VPos_y *= -1
                elif self.bola.bola_Rect.centery < bloco.bottom and bloco.top < self.bola.bola_Rect.centery:
                    self.bola.VPos_x *= -1
                else:
                    self.bola.VPos_y *= 1 
                    self.bola.VPos_x *= 1

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    os._exit(0)

            self.relogio.tick(60)
            self.layout()

            if self.jogo_iniciado:
                self.verificar_colisao()
                self.colisao_player_player2()
                self.bola.atualizar()

                if self.modo_jogador == "Player1":
                    self.exibir_nivel()
                    self.exibe_melhor_pontuacao()
                    self.exibir_pontuacao()
                    self.player.player_colisao()
                    self.player.input_player()
                    #self.bot.bot_executar_acoes()

                elif self.modo_jogador == "Player2":
                    self.exibir_nivel()
                    self.exibe_melhor_pontuacao2()
                    self.exibir_pontuacao2()
                    self.player.player_colisao()
                    self.player.input_player()
                    self.player2.player_colisao()
                    self.player2.input_player2()

            self.mensagem_fim_de_nivel()
            pygame.display.update()
            
    def layout(self):
        self.tela.fill((0,0,0)) # Se tu tirar daqui vai ferrar a animação!!!
        self.desenho_borda()
        self.botoes_tela_inicial_modos()
        self.selecao_de_modos_estrutura()

        if self.jogo_iniciado:
            self.desenho_borda()
            #self.bola.animacao_borda_bola()
            self.bola.desenho_bola()
            self.blocos.desenhar_blocos()

            if self.modo_jogador == "Player1":
                self.player.desenho_player()
                #self.bot.bot_desenho_player()

            elif self.modo_jogador == "Player2":
                self.player.desenho_player()
                self.player2.desenho_player()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()


