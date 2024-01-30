

from block_bricks import Jogo


def test_assert_verifica_altura_bola():
    jogo = Jogo()
    jogo.ball.y = jogo.height - jogo.relative_height_ball - jogo.ball.raio - 1
    jogo.verify_height_ball()
    assert jogo.mens_game_over

def test_particao_verificar_colisao():
    pass
