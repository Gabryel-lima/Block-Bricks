
import csv
import pygame
from pygame.locals import K_a, K_d
from player import Player

class ColetaDados:
    def __init__(self, tela, borda, largura, altura):
        self.player = Player(tela, borda, largura, altura)
        self.coletados = {'dados': []}  # Inicialize como um dicionário com a chave 'dados'
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
        pos_bola = {'x': pos_x, 'y': pos_y, 'acao': acao}
        self.coletados['dados'].append(pos_bola)

    def salva_dados(self):
        with open('src/coletadds.csv', 'w', newline='') as file:
            fieldnames = ['acao', 'x', 'y']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for data in self.coletados['dados']:
                writer.writerow(data)



