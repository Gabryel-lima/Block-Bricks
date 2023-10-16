
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder

class ColetaDados:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def coletar_dados(self):
        # Carregue o arquivo CSV em um DataFrame
        df = pd.read_csv(self.csv_path)

        return df

class Bot:
    def __init__(self):
        self.dtr = DecisionTreeRegressor(criterion='squared_error', random_state=50)
        self.coleta_dados = ColetaDados('src/coletadds.csv')
        self.label_encoder = LabelEncoder()

    def treinar_bot(self):
        # Coleta os dados
        dados = self.coleta_dados.coletar_dados()

        # Exiba as primeiras linhas do DataFrame
        print(dados.head())

        # Defina as colunas corretamente
        X = dados.drop(['acao'], axis=1)
        y = self.label_encoder.fit_transform(dados['acao'])

        smt = SMOTE(random_state=150)
        X_resampled, y_resampled = smt.fit_resample(X, y)

        X_resampled_df = pd.DataFrame(X_resampled, columns=X.columns)
        y_resampled_df = pd.DataFrame(y_resampled, columns=['acao'])

        # Treine seu modelo DecisionTreeRegressor com X_resampled e y_resampled
        self.dtr.fit(X_resampled_df, y_resampled_df)

        dados_final = pd.concat([X_resampled_df, y_resampled_df], axis=1)

        fi = self.dtr.feature_importances_

        predito_Arv = self.dtr.predict(X_resampled_df)

        print(fi)
        print(predito_Arv)

        # Exiba todas as linhas do DataFrame
        with pd.option_context('display.max_rows', None):
            print(dados_final)

if __name__ == "__main__":
    bot = Bot()
    bot.treinar_bot()
