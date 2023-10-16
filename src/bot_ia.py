
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.tree import DecisionTreeRegressor

class ColetaDados:
    def __init__(self, json_path):
        self.json_path = json_path

    def coletar_dados(self):
        # Carregue o arquivo JSON em um DataFrame
        df = pd.read_json(self.json_path)

        dado = {
            'pos_bola': [{'x': 1, 'y': 2, 'acao': 'parado'},
                        {'x': 3, 'y': 4, 'acao': 'direita'},
                        {'x': 5, 'y': 6, 'acao': 'esquerda'}]
        }

        df = pd.DataFrame(dado)

        # Aplique get_dummies à coluna 'pos_bola'
        dummie_dados = pd.get_dummies(df.drop(['pos_bola'], axis=1))
        return dummie_dados

class Bot:
    def __init__(self):
        self.dtr = DecisionTreeRegressor(criterion='squared_error', random_state=50)
        self.coleta_dados = ColetaDados('src/coletadds.json')

    def treinar_bot(self):
        # Coleta os dados
        dados = self.coleta_dados.coletar_dados()

        # Defina as colunas corretamente
        X = dados.drop(['pos_bola'], axis=1)
        y = dados['pos_bola']

        smt = SMOTE(random_state=150)
        X, y = smt.fit_resample(X, y)
        
        # Treine seu modelo DecisionTreeRegressor com X_resampled e y_resampled
        self.dtr.fit(X, y)

        dados_final = pd.concat([X, y], axis=1)

        print(dados_final.head(2))

if __name__ == "__main__":
    bot = Bot()
    bot.treinar_bot()