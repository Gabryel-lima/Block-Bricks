
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

class ColetaDados:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def coletar_dados(self):
        df = pd.read_csv(self.csv_path)
        return df

class TreinarModelo:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.dtc = DecisionTreeClassifier(random_state=50)
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

        self.X = self.dados_df.drop(['acao'], axis=1)
        self.y = self.dados_df['acao']

        self.smt = SMOTE(random_state=166)
        self.X_resampled, self.y_resampled = self.smt.fit_resample(self.X, self.y)

        self.X_treino, self.X_teste, self.y_treino, self.y_teste = train_test_split(self.X_resampled, self.y_resampled, test_size=0.2, random_state=43)

        self.dtc.fit(self.X_treino, self.y_treino)

        dados_final = pd.concat([self.X_treino, self.y_treino], axis=1)

        with pd.option_context('display.max_rows', 1312):
            print(dados_final.head(1312))

        predito_Arv = self.dtc.predict(self.X_teste)

        # Avaliação do modelo
        self.cmx = confusion_matrix(self.y_teste, predito_Arv)
        print("\nMatriz de Confusão:\n", self.cmx)

        self.acuracia = accuracy_score(self.y_teste, predito_Arv)
        print(f"\nAcuracia do modelo: {100 * self.acuracia:.2f}%\n")

        self.precisao = precision_score(self.y_teste, predito_Arv, average=None)
        for classe, p in enumerate(self.precisao):
            print(f"Precisao da classe {self.precisao} : {100 * p:.2f}%")

        print()

        self.recall = recall_score(self.y_teste, predito_Arv, average=None)
        for classe, i in enumerate(self.recall):
            print(f"Recall da classe {classe} : {100 * i:.2f}%")

if __name__ == "__main__":
    treino = TreinarModelo('src/coletadds.csv')
    treino.treinar_bot()
