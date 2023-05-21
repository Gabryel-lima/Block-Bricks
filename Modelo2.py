import pygame
from pygame.locals import *
from sys import exit

#Dando movimento ao retângulo.

pygame.init() #Inicializa os pacotes necessários do pygame.

largura = 640
altura = 480

x = 0
y = 0

tela = pygame.display.set_mode((largura, altura)) #O estilo de tela.
pygame.display.set_caption('Jogo') #Define o nome do jogo na janela.

while True: #Loop principal do jogo

    for event in pygame.event.get(): #Loop for para saber quando o jogador for sair do jogo.
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    pygame.draw.rect(tela, (255,0,0), (200,300,40,50)) #Desenhando um retângulo e definindo Tela, RGB, eixo x, eixo y, largura do retângulo e altura. Lembrando que o y é para baixo e o x para a direita a partir da origem.

    pygame.display.update() #Vai gerenciar a atualização do jogo.

