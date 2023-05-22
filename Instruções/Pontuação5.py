import pygame
from pygame.locals import *
from sys import exit
from random import randint #Uma biblioteca que sorteia valores dentro de um determinado interválo.

#Configurando uma colisão entre dois retângulos.

pygame.init() #Inicializa os pacotes necessários do pygame.

largura = 640
altura = 480

x = largura / 2 #Definindo desta forma conseguimos centralizar os objetos. 
#MEIO = largura_tela/2 - largura_objeto/2 'Caso fosse definir o objeto no meio corretamente.' 
y = altura / 2 #Definindo a altura, sem centralizar ele totalmente como no exemplo acima.

x_azul = randint(40, 600) #É bom se atentar a não usar um tamanho sorteado do mesma ordem da tela, senão o objeto ficará escondido.
y_azul = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True) #Definindo uma fonte para a pontuação em SysFont 1° o tipo, tamanho, negrito, itálico.

tela = pygame.display.set_mode((largura, altura)) #O estilo de tela.
pygame.display.set_caption('Jogo') #Define o nome do jogo na janela.
relogio = pygame.time.Clock() #Definindo uma var para atualização de tela.

while True: #Loop principal do jogo.

    relogio.tick(30) #Definindo o fps.
    tela.fill('Black') #Definindo uma cor de fundo.
    mensagem = f'Pontos: {pontos}' #Definindo uma mensagem de pontuação dentro do loop.
    texto_formatado = fonte.render(mensagem, False, (255,255,255)) #Uma var que vai formatar o texto e renderizar. 1° a mensagem como acima vai nele, pixelado, cor. 
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

    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50)) #Desenhando um retângulo e definindo Tela, RGB, eixo x, eixo y, largura do retângulo e altura. Lembrando que o y é para baixo e o x para a direita a partir da origem.
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50)) #Armazanando esses retângulos em vars para aplicar colisão. #E utilizando a vars sorteadas.

    if ret_vermelho.colliderect(ret_azul): #Esse colliderect verifica se houve colisão entre dois retângulos.
        x_azul = randint(40, 600) #Agora toda vez que a colisão ocorrer o retângulo azul mudará de posição.
        y_azul = randint(50, 430)
        pontos += 1 #Toda vez que houver uma colisão essa var vai receber ela mais 1.

    tela.blit(texto_formatado, (410,40)) #O blit exibe o texto formatado na tela. 1° o texto, eixo x, eixo y
    pygame.display.update() #Vai gerenciar a atualização do jogo.

