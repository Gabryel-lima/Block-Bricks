
import json
import pygame
from pygame.locals import K_a, K_d
from player import Player

class ColetaDados:
    def __init__(self, tela, borda, largura, altura):
        self.player = Player(tela, borda, largura, altura)
        self.coletados = []
        self.coleta_intervalo = 1000 
        self.coleta_tempo_acumulado = 0

    def verifica_direcao(self):
        if pygame.key.get_pressed()[K_a]:
            return 'esquerda'
        elif pygame.key.get_pressed()[K_d]:
            return 'direita'
        else:
            return 'parado'
        
    def coletar_dados(self, pos_x, pos_y):
        acao = self.verifica_direcao()
        pos_bola = (pos_x, pos_y)
        self.coletados.append({'acao': acao, 'pos_bola': pos_bola})

    def salva_dados(self):
        data = {'dados': self.coletados}
        with open('src/coletadds.json', 'w') as file:
            json.dump(data, file)
                