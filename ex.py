import pygame
from pygame.locals import *

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Exemplo de Botão')

cor_botao = (0, 255, 0)  # verde
cor_botao_hover = (0, 200, 0)  # verde mais escuro quando o mouse estiver sobre o botão

class Botao:
    def __init__(self, x, y, largura, altura, cor_normal, cor_hover, texto, acao):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor_normal = cor_normal
        self.cor_hover = cor_hover
        self.texto = texto
        self.acao = acao

    def desenhar(self, tela):
        cor = self.cor_hover if self.rect.collidepoint(pygame.mouse.get_pos()) else self.cor_normal
        pygame.draw.rect(tela, cor, self.rect)
        fonte = pygame.font.SysFont(None, 30)
        texto = fonte.render(self.texto, True, (255, 255, 255))
        texto_rect = texto.get_rect(center=self.rect.center)
        tela.blit(texto, texto_rect)

def lidar_eventos():
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()
        elif evento.type == MOUSEBUTTONDOWN:
            if botao_jogar.rect.collidepoint(pygame.mouse.get_pos()):
                print('Modo de jogo selecionado: Jogar')
            elif botao_opcoes.rect.collidepoint(pygame.mouse.get_pos()):
                print('Modo de jogo selecionado: Opções')

pygame.display.update()

botao_jogar = Botao(200, 200, 200, 100, cor_botao, cor_botao_hover, 'Jogar', 'jogar')
botao_opcoes = Botao(400, 200, 200, 100, cor_botao, cor_botao_hover, 'Opções', 'opcoes')

while True:
    tela.fill((0, 0, 0))  # Preenche a tela com preto
    botao_jogar.desenhar(tela)
    botao_opcoes.desenhar(tela)
    lidar_eventos()
    pygame.display.update()
