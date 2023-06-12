
import json
import os
import pygame
from pygame.locals import *

from jogo_base import JogoBase

class Jogo(JogoBase):
    def __init__(self):
        super().__init__()
        self.icon = pygame.image.load('assets/logo.ico')
        pygame.display.set_caption('Block-Bricks')
        pygame.display.set_icon(self.icon)
        self.relogio = pygame.time.Clock()
        self.pontos = 0
        self.som_fim_nivel = pygame.mixer.Sound('sounds/som_fim_nivel.wav')
        self.fim_jogo = pygame.mixer.Sound('sounds/som_de_fim.wav')
        self.som_colisao = pygame.mixer.Sound('sounds/encosta_bloco.wav')
        self.mesgc = f'"A"<Esquerda, "D">Direita, "LShift"<Aceleração>'
        self.nivel = 1
        self.mesg_nivel = f'Nivel: {self.nivel}'
        self.mesg = f'Pontos: {self.pontos}'
        self.lp = self.carregar_melhor_pontuacao()
        self.mesg_bp = f'Melhor pontuação: {self.lp}' 
        self.fontei = pygame.font.SysFont('Candara', 30, True, False)
        self.jogo_iniciado = False

    def verificar_colisao(self):
        if self.bola.rect.colliderect(self.player.rect) or self.bola.rect.colliderect(self.player2.rect):
            self.bola.inverter_direcao()

        if self.bola.y + self.bola.raio >= self.altura - 180:
            texto_formatado = self.fonte.render(f'Fim de jogo!', False, (255,255,255))  
            self.tela.blit(texto_formatado, (215,225))

            self.particao_verificar_colisao()
            
        for bloco in self.blocos.blocos:
            if self.bola.rect.colliderect(bloco):
                self.bola.inverter_direcaoB()
                self.som_da_bola_e_bloco()
                self.atualiza_pontuacao()
                self.atualiza_melhor_pontuacao()
                self.blocos.blocos.remove(bloco)
                break  # Adicionado para sair do loop após a colisão

    def particao_verificar_colisao(self):
        self.som_de_fim_de_jogo()
        pygame.display.flip()
        pygame.time.delay(3000)
        self.salvar_melhor_pontuacao()
        self.selecao_de_modos_estrutura_particao()
        self.blocos.resetar_blocos()
        self.bola.reset()
        self.bola.iniciar_movimento()
        self.player.reset()
        self.reset_pontos()
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
            with open('src/best_score.json', 'r') as file:
                data = json.load(file)
                return data['best_score']
        except (FileNotFoundError, KeyError):
            return 0

    def salvar_melhor_pontuacao(self):
        data = {'best_score': self.lp}
        with open('src/best_score.json', 'w') as file:
            json.dump(data, file)

    def atualiza_melhor_pontuacao(self):
        if self.pontos > self.lp:
            self.lp = self.pontos
            self.salvar_melhor_pontuacao()
            self.mesg_bp = f'Melhor pontuação: {self.lp}'

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

    def niveis_count(self):
        self.nivel += 1
        self.mesg_nivel = f'Nivel: {self.nivel}'

    def reset_nivel(self):
        if self.mensagem_fim_de_nivel == True:
            self.mesg_nivel = f'Nivel: {self.nivel}'
        else:
            self.nivel = 1
            self.mesg_nivel = f'Nivel: {self.nivel}'

    def reset(self): # Esse metodo retorna o menu.
        self.jogo_iniciado = False
        self.bola.reset()
        self.player.reset()
        self.rect_botao_player1 = pygame.Rect(240,170,100,30)
        self.rect_botao_player2 = pygame.Rect(240,230,100,35)

    def exibir_pontuacao(self):
        mensagem = self.mesg
        texto_formatado = self.fontei.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (40,430))

    def exibir_nivel(self):
        mensagem = self.mesg_nivel
        texto_formatado = self.fontei.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (40,480))

    def exibe_melhor_pontuacao(self):
        mensagem = self.mesg_bp
        texo_formatado = self.fontei.render(mensagem, False, (255,255,255))
        self.tela.blit(texo_formatado, (40,530))

    def mensagem_fim_de_nivel(self):
        if len(self.blocos.blocos) == 0:
            texto_formatado = self.fonte.render(f'Fim do Nivel {self.nivel}', False, (255,255,255))  
            self.tela.blit(texto_formatado, (self.altura // 2 - 100, self.largura // 2 - 80))
            self.niveis_count()
            self.som_de_fim_de_nivel()
            pygame.display.flip()
            pygame.time.delay(3000)
            self.blocos.resetar_blocos()
            self.reset()
            self.continuar_prox_nivel()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    os._exit(0)

            self.relogio.tick(60)
            self.layout()

            if self.jogo_iniciado:
                self.exibe_melhor_pontuacao()
                self.exibir_nivel()
                self.exibir_pontuacao()
                self.verificar_colisao()
                self.bola.atualizar()
                self.player.player_colisao()
                self.player.input_player()
                #self.player2.input_player2()

            self.mensagem_fim_de_nivel()
            pygame.display.update()

    def layout(self):
        self.tela.fill((0,0,0))
        self.desenho_borda()
        self.botoes_tela_inicial_modos()
        self.selecao_de_modos_estrutura()

        if self.jogo_iniciado == True:
            self.bola.desenho_bola()
            self.blocos.desenhar_blocos()
            self.player.desenho_player()
            #self.player2.desenho_player()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()

