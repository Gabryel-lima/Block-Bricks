# Documentação do código "Block-Bricks"

## Descrição

O código implementa um jogo de blocos com uma bola e um jogador que se move horizontalmente. O objetivo é quebrar todos os blocos sem deixar a bola cair do lado de baixo da tela. O jogador pode usar teclas para mover-se horizontalmente para desviar a bola e evitar que ela caia. O jogo tem diferentes níveis e a dificuldade aumenta a cada nível.

## Dependências

Para executar o código, é necessário instalar o Pygame.

## Classes

### Jogo

* `__init__(self)`: Inicia todas as variáveis de instância:
  * A janela do jogo
  * Descritores de tela
  * O movimento da bola
  * O jogador
  * Os blocos a serem quebrados
  * O som do jogo
* `verificar_colisao(self)`: Verifica se houve colisão da bola com o jogador ou um bloco. Se ocorrer a colisão com o jogador, a bola inverte a direção. Se ocorrer a colisão com um bloco, o bloco é quebrado, a bola inverte a direção e a pontuação do jogador é atualizada.
* `som_da_bola_e_bloco(self)`: Produz o som da bola colidindo com um bloco.
* `som_de_fim_de_jogo(self)`: Produz o som de fim de jogo.
* `som_de_fim_de_nivel(self)`: Produz o som de fim de nível.
* `reset(self)`: Reinicia o jogo.
* `class TelaInicial`: Herda da classe Jogo e define a tela de inicialização do jogo.
* `exibir_mensagem(self, texto, posicao)`: Exibe uma mensagem na tela.
* `exibir_pontuacao(self)`: Exibe a pontuação do jogador.
* `exibir_nivel(self)`: Exibe o nível atual do jogador.
* `mensagem_fim_de_jogo(self)`: Exibe a mensagem de fim de nível se houver quebrado todos os blocos, senão retorna nada.
* `atualiza_pontuacao(self)`: Atualiza a pontuação do jogador.
* `reset_pontos(self)`: Reinicia a pontuação do jogador para zero se necessário.
* `niveis_count(self)`: Aumenta o número do nível.
* `run(self)`: Função principal que controla a atualização da tela e eventos.

### Bola

* `__init__(self, jogo)`: Inicia todas as variáveis de instância e define a posição e velocidade da bola.
* `iniciar_movimento(self)`: Faz com que a bola comece a se mover.
* `atualizar(self)`: Atualiza a posição da bola.
* `inverter_direcao(self)`: Inverte o movimento da bola se ela colidir com o jogador.
* `inverter_direcaoB(self)`: Inverte o movimento da bola se ela colidir com um bloco.
* `reset(self)`: Reinicia a posição e velocidade da bola.

### Player

* `__init__(self, jogo, borda)`: Inicia todas as variáveis de instância e define a posição do jogador.
* `input_player(self)`: Verifica se o jogador quer se mover para a esquerda ou para a direita.
* `player_colisao(self)`: Verifica se a posição atual do jogador está dentro dos limites da game window.
* `reset(self)`: Reinicia a posição do jogador.

### Blocos

* `__init__(self, jogo)`: Inicia todas as variáveis de instância e define a posição dos blocos.
* `criar_blocos(self)`: Cria os blocos na tela.
* `desenhar_blocos(self)`: Desenha os blocos na tela.
* `resetar_blocos(self)`: Remove os blocos que foram quebrados e cria novos blocos para uma nova partida.

### criacao_niveis

* `__init__(self)`: Herda da classe Jogo, Bola e Blocos.

## Principais Métodos

* `__init__(self)`: Inicia todas as variáveis de instância.
* `verificar_colisao(self)`: Verifica se houve colisão da bola com o jogador ou um bloco.
* `reset(self)`: Reinicia o jogo.
* `run(self)`: Função principal que controla a atualização da tela e eventos.
* `iniciar_movimento(self)`: Faz com que a bola comece a se mover.
* `atualizar(self)`: Atualiza a posição da bola.
* `input_player(self)`: Verifica se o jogador quer se mover para a esquerda ou para a direita.
* `player_colisao(self)`: Verifica se a posição atual do jogador está dentro dos limites da game window.
* `reset_pontos(self)`: Reinicia a pontuação do jogador para zero se necessário.

## Utilização

Para jogar o game, execute o arquivo  **Block-Bricks.py** .

## Autores

O código foi desenvolvido por Gabryel Lima da Silva.
