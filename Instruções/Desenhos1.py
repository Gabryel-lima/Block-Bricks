import pygame
from pygame.locals import *
from sys import exit


pygame.init() #Inicializa os pacotes necessários do pygame.

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura)) #O estilo de tela.
pygame.display.set_caption('Jogo') #Define o nome do jogo na janela.

while True: #Loop principal do jogo

    for event in pygame.event.get(): #Loop for para saber quando o jogador for sair do jogo.
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    pygame.draw.rect(tela, (255,0,0), (200,300,40,50)) #Desenhando um retângulo e definindo Tela, RGB, eixo x, eixo y, largura do retângulo e altura. Lembrando que o y é para baixo e o x para a direita a partir da origem.

    pygame.draw.circle(tela, (0,0,255), (300,260), 40) #Desenhando um círculo e definindo Tela, RGB, exixo x e eixo y são referênciados no meio do círculo, por fim o seu raio.

    pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5) #Desenhando uma reta e definindo Tela, RGB, primeiro ponto da reta, segundo ponto da reta e expessura da reta. Lembrando a ordem diferentes dos eixos a prtir da origem.

    pygame.display.update() #Vai gerenciar a atualização do jogo.

