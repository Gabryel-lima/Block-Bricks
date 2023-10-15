
from sklearn.tree import DecisionTreeRegressor
from coleta_dados import ColetaDados

class Bot:
    def __init__(self):
        self.dtr = DecisionTreeRegressor()
        
    def treinar_bot(self):
        # Coletar dados de treinamento usando uma função adequada
        X_treino, y_treino = ColetaDados()
        
        # Treinar o modelo
        self.dtr.fit(X_treino, y_treino)

    def tomar_acao(self, estado_jogo):
        # Usar o modelo treinado para prever a ação com base no estado do jogo
        acao_numerica = self.dtr.predict(estado_jogo)
        # Converter ação numérica em ação real
        acao_real = [acao for acao, valor in self.dict_movimento.items() if valor == acao_numerica]
        return acao_real
