# Parte 1


""" Na função Player_colisao(), a linha self.jogo.x = self.colisao.right - self.player.width é responsável por ajustar a posição do jogador caso ele ultrapasse a borda direita da tela.

Vamos analisar essa linha em detalhes:

self.jogo.x: É a posição atual do jogador no eixo x.

self.colisao.right: É a coordenada do lado direito da área delimitada pela borda.

self.player.width: É a largura do retângulo do jogador.

A expressão self.colisao.right - self.player.width calcula a posição máxima que o jogador pode ter sem ultrapassar a borda direita. Se o jogador estiver além dessa posição máxima, ou seja, se self.player.right for maior que self.colisao.right, a linha ajusta a posição self.jogo.x para que o jogador fique exatamente na borda direita.

Isso garante que o jogador não ultrapasse a borda direita e permaneça visível dentro da área delimitada pelas bordas. """

'''Importações: Importei apenas os módulos necessários do pygame (pygame e pygame.locals) e o módulo exit do pacote sys.

Classe Jogo: Na inicialização da classe, adicionei a criação de um objeto pygame.Rect chamado borda que representa a borda da área do jogo. Removi a linha self.titulo e defini o título diretamente usando pygame.display.set_caption. Também adicionei um objeto pygame.time.Clock() chamado relogio para controlar a taxa de atualização do jogo.

Método run(): Adicionei uma chamada ao método layout() no início do loop principal do jogo. Em seguida, movi a criação dos objetos Player, Bola e Blocos para antes do loop principal. Isso evita que esses objetos sejam criados a cada iteração do loop.

Método layout(): Modifiquei esse método para desenhar o jogador e a bola com base nas coordenadas x e y dos respectivos objetos. Utilizei as propriedades self.player.x, self.player.y, self.bola.x e self.bola.y para obter as coordenadas atualizadas dos objetos. Os retângulos são desenhados usando pygame.draw.rect() e pygame.draw.circle().

Classe Player: Removi a linha que desenha o retângulo do jogador na inicialização da classe, pois agora o desenho é feito no método layout(). No método input_player(), atualizei as verificações de tecla pressionada para mover o jogador de forma mais suave, adicionando uma velocidade fracionada ao novo_x. Verifiquei se o novo valor de x está dentro dos limites da borda antes de atualizar a posição do jogador.

Classe Bola: No método atualizar(), atualizei a posição da bola com base nas velocidades velocidade_x e velocidade_y. Verifiquei se a bola atingiu as bordas da área do jogo e inverti a direção das velocidades quando necessário.'''

---

## Parte 2


Esse código é uma implementação básica de um jogo chamado "Block-Bricks" usando a biblioteca Pygame em Python. Vou explicar cada parte do código passo a passo:

1. Importações e definição da classe `Jogo`:

   - O código começa importando o módulo `pygame` para criar a interface do jogo.
   - Em seguida, é definida a classe `Jogo`, que representa o jogo em si.
   - No método `__init__`, várias configurações são feitas, como inicialização do Pygame, definição do título da janela, criação do objeto de relógio, definição das dimensões da tela, definição da fonte para exibição de texto, criação da tela principal, criação de uma área de borda retangular, criação do objeto jogador (`Player`), criação do objeto bola (`Bola`) e criação do objeto blocos (`Blocos`).
   - O atributo `jogo_iniciado` é inicializado como `False`, indicando que o jogo ainda não começou.
2. Método `run`:

   - O método `run` é responsável por iniciar o loop principal do jogo.
   - O loop principal é executado indefinidamente até que o jogo seja encerrado.
   - Dentro do loop, eventos são capturados e tratados.
   - Se o jogo ainda não foi iniciado e o evento for pressionar a tecla Enter (`K_RETURN`), o jogo é iniciado e o movimento da bola é iniciado.
   - O método `layout` é chamado para desenhar a tela do jogo.
   - Se o jogo estiver iniciado, são chamados métodos para capturar a entrada do jogador, verificar colisões, atualizar a posição da bola e verificar colisões novamente.
   - Por fim, a tela é atualizada para exibir as mudanças feitas.
3. Método `layout`:

   - O método `layout` é responsável por desenhar os elementos na tela.
   - Ele preenche a tela com a cor preta (`(0,0,0)`).
   - Se o jogo ainda não foi iniciado, uma mensagem é exibida no centro da tela.
   - Em seguida, desenha a bola como um círculo branco na posição atual da bola.
   - Desenha o jogador como um retângulo vermelho na posição atual do jogador.
   - Por fim, desenha a borda retangular ao redor da tela.
4. Método `exibir_mensagem`:

   - O método `exibir_mensagem` é usado para exibir mensagens na tela.
   - Ele recebe o texto da mensagem e a posição central da mensagem como parâmetros.
   - A mensagem é renderizada usando uma fonte e cor específicas e, em seguida, é desenhada na tela na posição especificada.
5. Método `verificar_colisao`:

   - O método `verificar_colisao` é responsável por verificar as colisões entre a bola e o jogador ou a borda inferior da tela.
   - Se houver uma colisão entre a bola e o jogador, a direção vertical da bola é invertida.
   - Se a bola atingir a borda inferior da tela, o método `reset` é chamado para reiniciar o jogo.
6. Método `reset`:

   - O método `reset` reinicia o jogo para o estado inicial.
   - O

 jogo é definido como não iniciado, a bola e o jogador são reposicionados para as posições iniciais.

7. Classe `Player`:

   - A classe `Player` representa o jogador no jogo.
   - No método `__init__`, o jogador é inicializado com uma posição inicial e um retângulo que o envolve.
   - O método `input_player` captura a entrada do jogador pelas teclas "A" e "D" para mover o jogador para a esquerda e para a direita, respectivamente.
   - O método `player_colisao` verifica se o jogador está dentro dos limites da borda do jogo e ajusta sua posição se necessário.
   - O método `reset` reposiciona o jogador para a posição inicial.
8. Classe `Bola`:

   - A classe `Bola` representa a bola no jogo.
   - No método `__init__`, a bola é inicializada com uma posição inicial, velocidades iniciais e um retângulo que a envolve.
   - O método `iniciar_movimento` é chamado quando o jogo é iniciado e define as velocidades iniciais da bola.
   - O método `atualizar` atualiza a posição da bola de acordo com suas velocidades.
   - Se a bola atingir as bordas esquerda ou direita da tela, a direção horizontal é invertida.
   - Se a bola atingir a borda superior da tela, a direção vertical é invertida.
   - O método `inverter_direcao` inverte a direção vertical da bola.
   - O método `reset` reposiciona a bola para a posição inicial.
9. Classe `Blocos`:

   - A classe `Blocos` representa os blocos do jogo, mas não há implementação para essa classe neste código.
10. Bloco principal de execução:

    - O bloco principal de execução cria um objeto `Jogo` e chama o método `run` para iniciar o jogo.

Espero que esta explicação passo a passo tenha sido útil para entender o funcionamento do código. Se você tiver alguma dúvida específica sobre algum ponto, sinta-se à vontade para perguntar!

---
