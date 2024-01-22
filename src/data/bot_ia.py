

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#from tensorflow import keras 

"""Problema de compatibilidade com a versão > Tensorflow 2.10!!!"""
class ColetaDados:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def coletar_dados(self):
        df = pd.read_csv(self.csv_path)
        return df

class TreinarModelo:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        #self.kra = keras
        self.df = None
        self.X = None
        self.X_resampled = None
        self.X_treino = None
        self.X_teste = None
        self.y = None
        self.y_resampled = None
        self.y_treino = None
        self.y_teste = None
        self.cmx = None
        self.acuracia = None
        self.precisao = None
        self.recall = None

    def ler_dados(self):
        coleta_dados = ColetaDados(self.csv_path)
        self.df = coleta_dados.coletar_dados()
        return self.df

    def treinar_bot(self):
        self.dados_df = self.ler_dados()

        self.X = self.dados_df[['x', 'y']].values
        self.y = self.dados_df['angle'].values
        
        self.norm = StandardScaler()
        self.X_resampled = self.norm.fit_transform(self.X)

        self.X_treino, self.X_teste, self.y_treino, self.y_teste = train_test_split(self.X_resampled, self.y)

        # Construa o modelo da rede neural
        # model = keras.Sequential([
        #     keras.layers.Dense(32, activation='elu', input_shape=(2,)),  # Duas entradas (x, y)
        #     keras.layers.Dropout(0.1),
        #     keras.layers.Dense(32, activation='elu'),
        #     keras.layers.Dropout(0.1),
        #     keras.layers.Dense(1)  # Uma saída (ângulo)
        # ])

        # Compile o modelo
        # model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])

        # # Treine o modelo
        # model.fit(self.X_treino, self.y_treino, epochs=100, batch_size=32, validation_split=0.2)

        # # Avalie o modelo

        # self.X_teste = self.norm.fit_transform(self.X_teste)
        # loss = model.evaluate(self.X_teste, self.y_teste)
        # print('\nErro Médio Quadrático (MSE): ', loss)

        # # Faça previsões
        # predictions = model.predict(self.X_teste)
        # print("\nPrevisão: ", predictions)

        # plt.figure(figsize=(10, 6))
        # plt.scatter(self.y_teste, predictions, c='r', label='Previsões')
        # plt.plot([self.y_teste.min(), self.y_teste.max()], [self.y_teste.min(), self.y_teste.max()], 'k--', lw=2, label='Linha de 45 graus')
        # plt.xlabel('Valor Real')
        # plt.ylabel('Previsão do Modelo')
        # plt.legend()
        # plt.title('Comparação entre Valores Reais e Previsões')
        # plt.show()

if __name__ == "__main__":
    treino = TreinarModelo('src/data/coletadds.csv')
    treino.treinar_bot()