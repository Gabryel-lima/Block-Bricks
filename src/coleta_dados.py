
import json
from player_base import PlayerBase

class ColetaDados:
    def __init__(self):
        self.player = PlayerBase()  # Crie uma instância de PlayerBase aqui
        self.dict_movimento = {'esquerda': 0, 'direita': 1, 'parado': 2}
        self.coletados = []
        self.verifica_direcao()
        self.coletar_dados()
        self.salva_dados()

    def verifica_direcao(self, direcao):
        if direcao in self.dict_movimento:
            return self.dict_movimento[direcao]
        return None

    def coletar_dados(self, direcao):
        acao_numerica = self.verifica_direcao(direcao)
        if acao_numerica is not None:
            self.coletados.append(acao_numerica)

    def salva_dados(self):
        data = {"acoes": self.coletados}
        with open('src/coletadds.json', 'w') as file:
            json.dump(data, file)
