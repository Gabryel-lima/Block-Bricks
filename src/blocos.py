

import pygame
from pygame.locals import *

import random

class Blocos:
    def __init__(self, jogo):
        self.jogo = jogo
        self.nivel_atual = 0
        self.nsort = random.randint(0,3)
        self.countr = random.randint(2,12)
        self.indice_aleatorio = []
        self.niveis = [
            (8,2),  # nível 1: (num_colunas, num_blocos_por_fileira)
            (8,3),  # nível 2
            (8,4),  # nível 3
            (8,5),  # nível 4
            (8,6),  # nível 5
            (8,7),  # nível 6
            (8,7),  # nível 7
            (8,8),  # nível 8
            (8,8),  # nível 9
            (8,8)  # nível 10
        ]
        self.configurar_nivel()

    def criar_blocos(self):
        for fileira in range(self.num_blocos_por_fileira):
            for coluna in range(self.num_colunas):
                x = self.espaco_blocos + coluna * (self.largura_bloco + self.espaco_blocos)
                y = self.espaco_blocos + fileira * (self.altura_bloco + self.espaco_blocos)
                self.bloco = pygame.Rect(x, y, self.largura_bloco, self.altura_bloco)
                self.blocos.append(self.bloco)

    def desenhar_blocos(self):
        for bloco in self.blocos:
            pygame.draw.rect(self.jogo.tela, (150,75,0), bloco, width=0, border_radius= 7)

    def resistencia_blocos(self):
        max_selecionados = min(self.countr, len(self.blocos))
        if max_selecionados >= len(self.blocos):
            max_selecionados = len(self.blocos) - 1
        
        self.indice_aleatorio = random.sample(range(len(self.blocos)), max_selecionados)
        print(self.indice_aleatorio)
        blocos_selecionados = [self.blocos[indice] for indice in self.indice_aleatorio]
        print(blocos_selecionados)

        self.blocos = [bloco for indice, bloco in enumerate(self.blocos) if indice not in self.indice_aleatorio]

        '''max_selecionados = min(self.countr, len(self.blocos)): Aqui, estamos calculando o número máximo de índices que podem ser selecionados. O valor é definido como o mínimo entre self.countr (que é o valor que determina quantos índices devem ser selecionados) e len(self.blocos) (que é o número total de blocos disponíveis).
        if max_selecionados >= len(self.blocos):: Nesta linha, estamos verificando se o número máximo de índices selecionados é maior ou igual ao número total de blocos disponíveis. Se isso for verdade, significa que poderíamos acabar selecionando todos os blocos, o que queremos evitar.
        max_selecionados = len(self.blocos) - 1: Se o número máximo de índices selecionados for maior ou igual ao número de blocos disponíveis, ajustamos o valor de max_selecionados para ser um valor menor, subtraindo 1 do número total de blocos.
        self.indice_aleatorio = random.sample(range(len(self.blocos)), max_selecionados): Aqui estamos usando a função random.sample para selecionar aleatoriamente max_selecionados índices da lista de blocos (self.blocos). Esses índices selecionados serão armazenados na lista self.indice_aleatorio.
        blocos_selecionados = [self.blocos[indice] for indice in self.indice_aleatorio]: Nesta linha, estamos criando uma nova lista chamada blocos_selecionados, que contém os blocos correspondentes aos índices selecionados em self.indice_aleatorio.
        self.blocos = [bloco for indice, bloco in enumerate(self.blocos) if indice not in self.indice_aleatorio]: Aqui estamos atualizando a lista de blocos (self.blocos) para remover os blocos correspondentes aos índices que foram selecionados aleatoriamente e armazenados em self.indice_aleatorio. Estamos usando uma compreensão de lista para criar uma nova lista de blocos que não inclui os blocos que foram selecionados.
        Essencialmente, esse método seleciona aleatoriamente um número de índices da lista de blocos, armazena esses índices e os blocos correspondentes em listas separadas, e então remove os blocos selecionados da lista original de blocos. Isso permite que você mantenha o controle dos blocos que foram selecionados e removidos para realizar as ações desejadas em seu jogo.'''

    def configurar_nivel(self):
        if self.nivel_atual < len(self.niveis):
            self.num_colunas, self.num_blocos_por_fileira = self.niveis[self.nivel_atual]
            self.espaco_blocos = 16
            self.largura_bloco = 57
            self.altura_bloco = 20
            self.countr = random.randint(2,18)
            self.blocos = []
            self.nivel_atual += 1
            self.criar_blocos()
            #self.resistencia_blocos()

    def resetar_blocos(self):
        self.blocos.clear()
        self.nivel = 0
        self.criar_blocos()
        #self.resistencia_blocos()
