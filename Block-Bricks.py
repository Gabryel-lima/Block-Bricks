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
        self.Tela = TelaInicial
        if self.bola.rect.colliderect(self.player.rect):
            self.bola.inverter_direcao()

        if self.bola.y + self.bola.raio >= self.altura - 180:
            texto_formatado = self.fonte.render(f'Fim de jogo!', False, (255,255,255))  
            self.tela.blit(texto_formatado, (215,225))
            self.som_de_fim_de_jogo()
            pygame.display.flip()
            pygame.time.delay(3000)
            self.Tela.selecao_de_modos_particao(self)
            self.blocos.resetar_blocos()
            self.bola.reset()
            self.bola.iniciar_movimento()
            self.player.reset()
            self.reset_pontos()
            self.reset_nivel()
            
        for bloco in self.blocos.blocos:
            if self.bola.rect.colliderect(bloco):
                self.bola.inverter_direcaoB()
                self.som_da_bola_e_bloco()
                self.atualiza_pontuacao()
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
        self.rect_botao_player1 = pygame.Rect(240,170,100,30)
        self.rect_botao_player2 = pygame.Rect(240,220,100,30)

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

class TelaInicial(Jogo):
    def __init__(self):
        super().__init__()
        self.modo1 = f'Player 1'
        self.modo2 = f'Player 2'
        self.back = f'Voltar'
        self.mesgite = f'Pressione a tecla "Enter" para iniciar' 
        self.largurab = self.largura
        self.alturab = self.altura
        self.cor_botao_modo1 = (255,255,255)
        self.cor_botao_modo2 = (255,255,255)
        self.cor_botao_voltar = (255,255,255)
        self.rect_botao_voltar = pygame.Rect(50,300,80,30)  
        self.rect_botao_player1 = pygame.Rect(240,170,100,35)
        self.rect_botao_player2 = pygame.Rect(240,230,100,35)

    def desenho_borda(self):
        pygame.draw.rect(self.tela, (115,115,115), self.borda, 3)

    def desenho_botao_back(self):
        pos_mouse = pygame.mouse.get_pos()
        rect_botao = self.rect_botao_voltar
        mensagem = self.back

        if rect_botao.collidepoint(pos_mouse):
            self.cor_botao_voltar = (150,150,150) 
        else:
            self.cor_botao_voltar = (255,255,255) 

        if self.rect_botao_voltar.width > 0 and self.rect_botao_voltar.width > 0:  
            texto_formatado1 = self.fonte.render(mensagem, False, self.cor_botao_voltar)
            self.tela.blit(texto_formatado1, (40,300))

    def botoes_tela_inicial(self):
        pos_mouse = pygame.mouse.get_pos()
        mod1 = self.modo1
        mod2 = self.modo2
        rect_modo1 = self.rect_botao_player1
        rect_modo2 = self.rect_botao_player2

        if rect_modo1.collidepoint(pos_mouse):
            self.cor_botao_modo1 = (150,150,150) 
        else:
            self.cor_botao_modo1 = (255,255,255)  

        if rect_modo2.collidepoint(pos_mouse):
            self.cor_botao_modo2 = (150,150,150) 
        else:
            self.cor_botao_modo2 = (255,255,255)  

        if self.rect_botao_player1.width > 0 and self.rect_botao_player2.width > 0:  
            texto_formatado1 = self.fonte.render(mod1, False, self.cor_botao_modo1)
            self.tela.blit(texto_formatado1, (240,170))
            texto_formatado2 = self.fonte.render(mod2, False, self.cor_botao_modo2)
            self.tela.blit(texto_formatado2, (240,230))

    def selecao_de_modos(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()

                if self.rect_botao_player1.collidepoint(pos_mouse) or self.rect_botao_player2.collidepoint(pos_mouse):
                    pygame.display.flip()
                    self.rect_botao_player1 = pygame.Rect(0,0,0,0)
                    self.rect_botao_player2 = pygame.Rect(0,0,0,0)
                    pygame.time.delay(1000)

                    self.selecao_de_modos_particao()

    def selecao_de_modos_particao(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    os._exit(0)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.jogo_iniciado = True
                    self.bola.iniciar_movimento()
                    return
                else:
                    self.tela.fill((0,0,0))
                    self.desenho_botao_back()
                    self.desenho_borda()
                    self.player.desenho_player()
                    self.bola.desenho_bola()
                    self.blocos.desenhar_blocos()
                    self.exibir_mensagem_inte_iniciar()
                    pygame.display.update()

    def continuar_prox_nivel(self):
        self.jogo_iniciado = True
        self.bola.iniciar_movimento()
        self.rect_botao_player1 = pygame.Rect(0,0,0,0)
        self.rect_botao_player2 = pygame.Rect(0,0,0,0)
        return

    def layout(self):
        self.tela.fill((0,0,0))
        self.desenho_borda()
        self.botoes_tela_inicial()
        self.selecao_de_modos()

        if self.jogo_iniciado == True:
            self.bola.desenho_bola()
            self.player.desenho_player()
            self.blocos.desenhar_blocos()

    def exibir_mensagem_inte_iniciar(self):
        mensagem = self.mesgite
        fonte = pygame.font.SysFont('times new roman', 25, True, False)
        texto_formatado = fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (100,205))

    def exibir_pontuacao(self):
        mensagem = self.mesg
        texto_formatado = self.fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (40,430))

    def exibir_nivel(self):
        mensagem = self.mesg_nivel
        texto_formatado = self.fonte.render(mensagem, False, (255,255,255))  
        self.tela.blit(texto_formatado, (40,480))

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
                self.exibir_nivel()
                self.exibir_pontuacao()
                self.verificar_colisao()
                self.player.input_player()
                self.bola.atualizar()

            self.mensagem_fim_de_nivel()
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
