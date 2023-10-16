import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class ColetaDados:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def coletar_dados(self):
        # Carregue o arquivo CSV em um DataFrame
        df = pd.read_csv(self.csv_path)

        return df

class Bot:
    def __init__(self):
        self.dtc = DecisionTreeClassifier(random_state=50)
        self.coleta_dados = ColetaDados('src/coletadds.csv')

    def treinar_bot(self):
        # Coleta os dados
        dados = self.coleta_dados.coletar_dados()

        # Defina as colunas corretamente
        X = dados.drop(['acao'], axis=1)
        y = dados['acao']

        smt = SMOTE(random_state=150)
        X_resampled, y_resampled = smt.fit_resample(X, y)

        # Dividir os dados em conjuntos de treinamento e teste
        X_treino, X_teste, y_treino, y_teste = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

        self.dtc.fit(X_treino, y_treino)

        dados_final = pd.concat([X_treino, y_treino], axis=1)

        with pd.option_context('display.max_rows', 1312):
            print(dados_final.head(1312))

        predito_Arv = self.dtc.predict(X_teste)

        # Avaliação do modelo
        cm = confusion_matrix(y_teste, predito_Arv)
        print("\nMatriz de Confusão:\n", cm)

        acuracia = accuracy_score(y_teste, predito_Arv)
        print(f"\nAcuracia do modelo: {100 * acuracia:.2f}S%")
        

if __name__ == "__main__":
    bot = Bot()
    bot.treinar_bot()
