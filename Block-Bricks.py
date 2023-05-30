import pygame
from pygame.locals import *
import os
import random

class Jogo:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Block-Bricks')
        self.relogio = pygame.time.Clock()
        self.largura = 600
        self.altura = 600
        self.pontos = 0
        self.som_fim_nivel = pygame.mixer.Sound('sounds/som_fim_nivel.wav')
        self.fim_jogo = pygame.mixer.Sound('sounds/som_de_fim.wav')
        self.som_colisao = pygame.mixer.Sound('sounds/encosta_bloco.wav')
        self.nivel = 1
        self.mesg_nivel = f'Nivel: {self.nivel}'
        self.mesg = f'Pontos: {self.pontos}'
        self.fonte = pygame.font.SysFont('arial', 30, True, False)
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.borda = pygame.Rect(0, 0, self.largura, self.altura)
        self.player = Player(self, self.borda, self.tela)
        self.bola = Bola(self, self.tela)
        self.blocos = Blocos(self)
        self.jogo_iniciado = False

    def verificar_colisao(self):
        if self.bola.rect.colliderect(self.player.rect):
            self.bola.inverter_direcao()

        if self.bola.y + self.bola.raio >= self.altura - 180:
            texto_formatado = self.fonte.render(f'Fim de jogo!', False, (255,255,255))  
            self.tela.blit(texto_formatado, (215,225))
            self.som_de_fim_de_jogo()
            pygame.display.flip()
            pygame.time.delay(3000)
            self.blocos.resetar_blocos()
            self.reset()
            self.reset_pontos()
            
        for bloco in self.blocos.blocos:
            if self.bola.rect.colliderect(bloco):
                self.atualiza_pontuacao()
                self.bola.inverter_direcaoB()
                self.som_da_bola_e_bloco()
                self.blocos.blocos.remove(bloco)
                break  # Adicionado para sair do loop após a colisão

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

    def reset(self):
        self.jogo_iniciado = False
        self.bola.reset()
        self.player.reset()

class TelaInicial(Jogo):
    def __init__(self):
        super().__init__()
        self.modo1 = f'Player 1'
        self.modo2 = f'Player 2'
        self.largurab = self.largura
        self.alturab = self.altura
        self.cor_modo1 = (255,255,255)  
        self.cor_modo2 = (255,255,255)
        self.rect1 = pygame.Rect(240,170,100,30)
        self.rect2 = pygame.Rect(240,220,100,30)

    def desenho_borda(self):
        pygame.draw.rect(self.tela, (115,115,115), self.borda, 3)

    def botoes_tela_inicial(self):
        pos_mouse = pygame.mouse.get_pos()
        mod1 = self.modo1
        mod2 = self.modo2
        rect_modo1 = self.rect1
        rect_modo2 = self.rect2

        if rect_modo1.collidepoint(pos_mouse):
            self.cor_modo1 = (150,150,150) 
        else:
            self.cor_modo1 = (255,255,255)  

        if rect_modo2.collidepoint(pos_mouse):
            self.cor_modo2 = (150,150,150) 
        else:
            self.cor_modo2 = (255,255,255)  

        if self.rect1.width > 0 and self.rect2.width > 0:  
            texto_formatado1 = self.fonte.render(mod1, False, self.cor_modo1)
            self.tela.blit(texto_formatado1, (240, 170))
            texto_formatado2 = self.fonte.render(mod2, False, self.cor_modo2)
            self.tela.blit(texto_formatado2, (240, 220))

    def selecao_de_modos(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                pos_mouse = pygame.mouse.get_pos()

                if not self.jogo_iniciado:
                    if self.rect1.collidepoint(pos_mouse):
                        self.rect1 = pygame.Rect(0,0,0,0)
                        self.jogo_iniciado = True
                        self.bola.iniciar_movimento()

                    elif self.rect2.collidepoint(pos_mouse):
                        self.rect2 = pygame.Rect(0,0,0,0)
                        self.jogo_iniciado = True
                        self.bola.iniciar_movimento()

                self.exibir_mensagem("Pressione 'Enter' para iniciar o jogo", (self.largura // 2, self.altura // 2))
                if event.type == KEYDOWN and event.key == K_RETURN:
                    self.jogo_iniciado = True
                    self.bola.iniciar_movimento()

    def layout(self):
        self.tela.fill((0,0,0))
        self.botoes_tela_inicial()
        self.selecao_de_modos()

        self.bola.desenho_bola()
        self.player.desenho_player()
        self.desenho_borda()
        self.blocos.desenhar_blocos()

    def exibir_mensagem(self, texto, posicao): # Bom exemplo de adaptação de texto no futuro.
        fonte = pygame.font.Font(None, 30)
        mensagem = fonte.render(texto, True, (255,255,255))
        retangulo = mensagem.get_rect()
        retangulo.center = posicao
        self.tela.blit(mensagem, retangulo)

    def exibir_pontuacao(self):
        mensagem = self.mesg
        texto_formatado = self.fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (40,430))

    def exibir_nivel(self):
        mensagem = self.mesg_nivel
        texto_formatado = self.fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (40,480))

    def mensagem_fim_de_jogo(self):
        if len(self.blocos.blocos) == 0:
            texto_formatado = self.fonte.render(f'Fim do Nivel {self.nivel}', False, (255,255,255))  
            self.tela.blit(texto_formatado, (self.altura // 2 - 100, self.largura // 2 - 80))
            self.niveis_count()
            self.som_de_fim_de_nivel()
            pygame.display.flip()
            pygame.time.delay(3000)
            self.blocos.resetar_blocos()
            self.reset()
            return
            
    def atualiza_pontuacao(self):
        self.pontos += 1
        self.mesg = f'Pontos: {self.pontos}'

    def reset_pontos(self):
        if self.mensagem_fim_de_jogo == True:
            self.mesg = f'Pontos: {self.pontos}'

        else:
            self.pontos = 0
            self.mesg = f'Pontos: {self.pontos}'

    def niveis_count(self):
        self.nivel += 1

    def run(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    os._exit(0)

            self.relogio.tick(60)
            self.layout()
            if self.jogo_iniciado:
                self.exibir_nivel()
                self.exibir_pontuacao()
                self.verificar_colisao()
                self.player.input_player()
                self.bola.atualizar()

            self.mensagem_fim_de_jogo()
            pygame.display.update()

class Bola:
    def __init__(self, jogo, tela):
        self.tela = tela
        self.jogo = jogo
        self.x = 300
        self.y = 350
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.raio = 5
        self.rect = pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio * 1, self.raio * 1)
        
    def desenho_bola(self):
        pygame.draw.circle(self.tela, (255,255,255), ((self.x), (self.y)), self.raio)

    def iniciar_movimento(self):
        self.velocidade_x = random.randint(-3,3) # random.randint(-5,5) 
        self.velocidade_y = random.choice([-2,-3,-4]) # random.choice([-3,-4,-5])
        self.rect.center = (self.x, self.y)

    def atualizar(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y
        self.rect.center = (self.x, self.y)

        if self.x - self.raio <= 0 or self.x + self.raio >= self.jogo.largura:
            self.velocidade_x *= -1

        if self.y - self.raio <= 0:
            self.velocidade_y *= -1      

    def inverter_direcao(self):
        if pygame.key.get_pressed()[K_a]:
            self.velocidade_y *= -1
            self.velocidade_x -= 1

        elif pygame.key.get_pressed()[K_d]:
            self.velocidade_y *= -1
            self.velocidade_x += 1
        else:
            self.velocidade_y *= -1
            self.velocidade_x *= 1

    def inverter_direcaoB(self):
        self.velocidade_y *= -1
        self.velocidade_x *= 1

    def reset(self):
        self.x = 300
        self.y = 350
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.rect.center = (self.x, self.y)

class Player:
    def __init__(self, jogo, borda, tela):
        self.tela = tela
        self.jogo = jogo
        self.colisao = borda
        self.x = self.jogo.largura // 2 - 40 // 2
        self.y = self.jogo.altura // 2 - 5 // 2 + 100
        self.rect = pygame.Rect(self.x, self.y, 40, 5)

    def desenho_player(self):
        pygame.draw.rect(self.tela, (255,0,0), ((self.x), (self.y), 40, 5))

    def input_player(self):
        novo_x = self.x
        if pygame.key.get_pressed()[K_a]:
            novo_x -= 3.5

            if pygame.key.get_pressed()[K_LSHIFT]:
                novo_x -= 5

        if pygame.key.get_pressed()[K_d]:
            novo_x += 3.5

            if pygame.key.get_pressed()[K_LSHIFT]:
                novo_x += 5

        if self.colisao.left <= novo_x <= self.colisao.right - 40:
            self.x = novo_x

        self.rect.x = self.x

    def player_colisao(self):
        if self.x < self.jogo.borda.left:
            self.x = self.jogo.borda.left

        if self.x + 40 > self.jogo.borda.right:
            self.x = self.jogo.borda.right - 40

        self.rect.x = self.x

    def reset(self):
        self.x = self.jogo.largura // 2 - 40 // 2
        self.rect.x = self.x

class PLayer2(Player):
    def __init__(self):
        super().__init__()
        pass

class Blocos:
    def __init__(self, jogo):
        self.jogo = jogo
        self.num_colunas = 4 #4
        self.num_blocos_por_fileira = 8 #8
        self.espaco_blocos = 16
        self.largura_bloco = self.num_blocos_por_fileira + 49 
        self.altura_bloco = 20
        self.blocos = []
        self.criar_blocos()

    def criar_blocos(self):
        for fileira in range(self.num_colunas):
            for coluna in range(self.num_blocos_por_fileira):
                x = self.espaco_blocos + coluna * (self.largura_bloco + self.espaco_blocos)
                y = self.espaco_blocos + fileira * (self.altura_bloco + self.espaco_blocos)
                bloco = pygame.Rect(x, y, self.largura_bloco, self.altura_bloco)
                self.blocos.append(bloco)

    def desenhar_blocos(self):
        for bloco in self.blocos:
            pygame.draw.rect(self.jogo.tela, (100,100,100), bloco)

    def resetar_blocos(self):
        self.blocos.clear()
        self.criar_blocos()

class criacao_niveis(Jogo,Bola,Blocos):
    def __init__(self):
        super.__init__()

    def nivel_1(self):
        pass

if __name__ == "__main__":
    jogo = TelaInicial()
    jogo.run()
