import pygame
from pygame.locals import *
from sys import exit

#Controle de movimento.

pygame.init() #Inicializa os pacotes necessários do pygame.

largura = 640
altura = 480

x = largura / 2 #Definindo desta forma conseguimos centralizar os objetos. 
#MEIO = largura_tela/2 - largura_objeto/2 'Caso fosse definir o objeto no meio corretamente.' 
y = altura / 2 #Definindo a altura, sem centralizar ele totalmente como no exemplo acima.

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
        
        '''if event.type == KEYDOWN: #Aqui define os movimentos com tecla assim que são realizados.
            if event.key == K_a:
                x -= 20

            if event.key == K_d:
                x += 20

            if event.key == K_w:
                y -= 20

            if event.key == K_s:
                y += 20'''

    if pygame.key.get_pressed()[K_a]: #Assim definimos uma movimentação contínua.
        x -= 20
        
    if pygame.key.get_pressed()[K_d]:
        x += 20

    if pygame.key.get_pressed()[K_w]:
        y -= 20

    if pygame.key.get_pressed()[K_s]:
        y += 20

    pygame.draw.rect(tela, (255,0,0), (x,y,40,50)) #Desenhando um retângulo e definindo Tela, RGB, eixo x, eixo y, largura do retângulo e altura. Lembrando que o y é para baixo e o x para a direita a partir da origem.
    

    pygame.display.update() #Vai gerenciar a atualização do jogo.

