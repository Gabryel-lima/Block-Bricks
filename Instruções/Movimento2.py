import pygame
from pygame.locals import *
from sys import exit

#Dando movimento ao retângulo.

pygame.init() #Inicializa os pacotes necessários do pygame.

largura = 640
altura = 480

x = largura / 2 #Definindo desta forma conseguimos centralizar os objetos. 
#MEIO = largura_tela/2 - largura_objeto/2 'Caso fosse definir o objeto no meio corretamente.' 
y = 0

tela = pygame.display.set_mode((largura, altura)) #O estilo de tela.
pygame.display.set_caption('Jogo') #Define o nome do jogo na janela.
relogio = pygame.time.Clock() #Definindo uma var para atualização de tela.

while True: #Loop principal do jogo.

    relogio.tick(30) #Definindo o fps.
    tela.fill('Black') #Definindo uma cor de fundo.
    for event in pygame.event.get(): #Loop for para saber quando o jogador for sair do jogo.
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (255,0,0), (x,y,40,50)) #Desenhando um retângulo e definindo Tela, RGB, eixo x, eixo y, largura do retângulo e altura. Lembrando que o y é para baixo e o x para a direita a partir da origem.
    
    if y >= altura:
        y = 0
    y += 1


    pygame.display.update() #Vai gerenciar a atualização do jogo.

