

from block_bricks import Jogo


def test_assert_verifica_altura_bola():
    jogo = Jogo()
    jogo.bola.y = jogo.altura - jogo.altura_relativa_bola - jogo.bola.raio - 1
    jogo.verifica_altura_bola()
    assert jogo.mesg_fj

def test_particao_verificar_colisao():
    pass
